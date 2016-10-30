from BSFC.apps.item.models import Item
from BSFC.apps.cost.models import Cost
from BSFC.apps.revenue.models import Revenue
from BSFC.public.timezone_convert import (
    convert_utc_to_pacific, convert_pacific_to_utc
)
from validation import validate_item
from validation import validate_line_item
from api_data import get_api_data
import time
from datetime import datetime, timedelta
import logging
from .constants import PACIFIC_TIMEZONE
import pytz
log = logging.getLogger('django')

# takes in a contiguous range of dates
def populate_single_day(dates):
    """use payments from the day to record quantity of each item contributing to revenue calculation"""
    for idx, date in enumerate(dates):
        todays_datetime = date
        tz = pytz.timezone(PACIFIC_TIMEZONE)
        todays_datetime_pacific = tz.localize(
            datetime(todays_datetime.year, todays_datetime.month,
                     todays_datetime.day, todays_datetime.hour, todays_datetime.minute,
                     todays_datetime.second, todays_datetime.microsecond),
            is_dst=None
        )
        pacific_datetime_beginning_of_day = tz.localize(
            datetime(todays_datetime.year, todays_datetime.month, todays_datetime.day, 0, 0, 0, 0),
            is_dst=None
        )
        pacific_datetime_end_of_day = tz.localize(
            datetime(todays_datetime.year, todays_datetime.month, todays_datetime.day, 23, 59, 59, 999999),
            is_dst=None
        )
        utc_datetime_beginning_of_day = convert_pacific_to_utc(pacific_datetime_beginning_of_day)
        utc_datetime_end_of_day = convert_pacific_to_utc(pacific_datetime_end_of_day)
        utc_datetime_beginning_of_day_ms = int(time.mktime(utc_datetime_beginning_of_day.timetuple())) * 1000
        utc_datetime_end_of_day_ms = int(time.mktime(utc_datetime_end_of_day.timetuple())) * 1000
        todays_payments = get_api_data(
            'payments',
            filterItems='createdTime>' + str(utc_datetime_beginning_of_day_ms) + '&createdTime<' + str(utc_datetime_end_of_day_ms),
            expandItems='order,refunds,tender'
        )
        #call to REST API to get list of all payments, expanding by 'order,' 'refunds,' and 'tender' and filtering by day

        for payment_dict in todays_payments:
            payment_type = payment_dict['tender']['label']
            order_id = payment_dict['order']['id']
            order_dict = get_api_data(
                'orders/' + str(order_id),
                expandItems='lineItems,discounts'
            )
            #get corresponding order with payment['order']['id'], expanding by 'lineItems,' 'discounts'
            # items = []
            for line_item_dict in order_dict['lineItems']['elements']:
                quantity = line_item_dict['unitQty']/1000.00 if 'unitQty' in line_item_dict else 1
                item_qs = Item.objects.filter(
                    name=line_item_dict['name'], created_at__gte=pacific_datetime_beginning_of_day, created_at__lte=pacific_datetime_end_of_day
                )
                if item_qs.exists():
                	item_qs[0].revenue.update_revenue_field(payment_type, quantity)
                else:
                    item_dict = validate_line_item(line_item_dict) #returns None if item_dict is validated properly; in that case proceed to make REST API call
                    if item_dict == None:
                        item_dict = get_api_data(
                        'items/' + str(line_item_dict['item']['id']),
                        expandItems='categories'
                    )

                    revenue_object = Revenue()
                    revenue_object.update_revenue_field(payment_type, quantity)
                    revenue_object.save()
                    item_dict = validate_item(item_dict)
                    cost = Cost.objects.create(item_cost=item_dict['cost'])
                    Item.objects.create(
                        name=item_dict['name'],
                        cost=cost,
                        price=item_dict['price'],
                        price_type=item_dict['priceType'],
                        unit_name=item_dict['unitName'] if 'unitName' in item_dict else None,
                        category=item_dict['categories']['elements'][0]['name'],
                        revenue=revenue_object,
                        created_at=todays_datetime_pacific
                    )
            # Item.objects.bulk_create(items)
        #print("Finished: " + str(idx))
