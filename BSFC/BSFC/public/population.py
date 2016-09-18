from BSFC.apps.item.models import Item
from BSFC.apps.cost.models import Cost
from BSFC.apps.revenue.models import Revenue
from validation import validate_item
from api_data import get_api_data
import time
from datetime import datetime, timedelta
import logging
log = logging.getLogger('django')

def populate_single_day():
    """use payments from the day to record quantity of each item contributing to revenue calculation"""
    todays_datetime = datetime.today()
    yesterday = todays_datetime + timedelta(days=-1)
    yesterday_timestamp_ms = int(time.mktime(yesterday.timetuple())) * 1000
    todays_payments = get_api_data(
        'payments',
        filterItems='createdTime>' + str(yesterday_timestamp_ms),
        expandItems='order,refunds,tender'
    )
    #call to REST API to get list of all payments, expanding by 'order,' 'refunds,' and 'tender' and filtering by day

    for payment_dict in todays_payments:
        todays_date = datetime.today()
        #whatever convention we are using for dates...?
        payment_type = payment_dict['tender']['label']
        order_id = payment_dict['order']['id']
        order_dict = get_api_data(
            'orders/' + str(order_id),
            expandItems='lineItems,discounts'
        )
        beginning_of_day = datetime(todays_datetime.year, todays_datetime.month, todays_datetime.day, 0, 0, 0, 0)
        end_of_day = datetime(todays_datetime.year, todays_datetime.month, todays_datetime.day, 23, 59, 59, 59)
        #get corresponding order with payment['order']['id'], expanding by 'lineItems,' 'discounts'
        for line_item_dict in order_dict['lineItems']['elements']:
            quantity = line_item_dict['unitQty']/1000 if 'unitQty' in line_item_dict else 1
            item_qs = Item.objects.filter(name=line_item_dict['name'], created_at__gte=beginning_of_day, created_at__lte=end_of_day)
            if item_qs.exists():
            	item_qs[0].revenue.update_revenue_field(payment_type, quantity)
            else:
                item_dict = get_api_data(
                    'items/' + str(line_item_dict['item']['id']),
                    expandItems='categories'
                )
                #call to REST API to get item; use line_item_dict['elements']['item']['id']
                revenue_object = Revenue()
                revenue_object.update_revenue_field(payment_type, quantity)
                revenue_object.save()
                item_dict = validate_item(item_dict)
                Item.objects.create(
                    name=item_dict['name'],
                    cost=Cost.objects.create(item_cost=item_dict['cost']),
                    price=item_dict['price'],
                    price_type=item_dict['priceType'],
                    unit_name=item_dict['unitName'] if 'unitName' in item_dict else None,
                    category=item_dict['categories']['elements'][0]['name'],
                    revenue=revenue_object
                )
