from BSFC.apps.item.models import Item
from BSFC.apps.cost.models import Cost
from BSFC.apps.revenue.models import Revenue
from BSFC.apps.discounts.models import Discounts

def populate_single_day():
	MEMBER = True; #used to update discount info
	NOT_MEMBER = False;

	"""use payments from the day to record quantity of each item contributing to revenue calculation"""
	todays_payments = #call to REST API to get list of all payments, expanding by 'order,' 'refunds,' and 'tender' and filtering by day

	for payment_dict in todays_payments:
		member_percentage = 0;
		other_percentage = 0;
		todays_date = #whatever convention we are using for dates...?
		payment_type = payment_dict['tender']['label']
		order_dict = #get corresponding order with payment['order']['id'], expanding by 'lineItems,' 'discounts'

		if 'discounts' in order_dict: #not including non-percentage discounts
			for discount_dict in order_dict['discounts']['elements']:
				if discount_dict['name'] == 'Member':
					member_percentage += discount_dict['percentage']/100
				elif 'percentage' in discount_dict:
					other_percentage += discount_dict['percentage']/100

		for line_item_dict in order_dict['lineItems']['elements']:
			line_item_expanded = #have to call REST API again using line_item_dict['id']to get lineItems individually in order to see discounts on indiv line items...worth it...?
			line_item_member_percentage = 0
			line_item_percentage = 0

			quantity = line_item_dict['unitQty']/1000 if 'unitQty' in line_item_dict else 1

			if 'discounts' in line_item_expanded:	
				for discount_dict in line_item_expanded['discounts']['elements']:		
					if discount_dict['name'] == 'Member':
						line_item_member_percentage += discount_dict['percentage']/100
					elif 'percentage' in discount_dict:
						line_item_other_percentage += discount_dict['percentage']/100

			if Item.objects.filter(name = line_item_dict['name'], created_at.date() = todays_date).exists():
				I = Item.objects.get(name = line_item_dict['name'], created_at.date() = todays_date)
				I.revenue.update_revenue_field(payment_type, quantity)
				I.discounts.update_discounts(quantity*(member_percentage + line_item_member_percentage - member_percentage*line_item_member_percentage - line_item_other_percentage*member_percentage), MEMBER)
				I.discounts.update_discounts(quantity*(other_percentage + line_item_other_percentage - other_percentage*line_item_other_percentage - line_item_member_percentage*other_percentage), NOT_MEMBER)


			else:
				item_dict = #call to REST API to get item; use line_item_dict['elements']['item']['id']
				Items.objects.create(name = item_dict['name'], cost = Cost.objects.create(item_cost = item_dict['cost']), price = item_dict['price'], price_type = item_dict['priceType'], unit_name = item_dict['unitName'] if 'unitName' in item_dict else None, category = item_dict['categories']['elements'][0]['name'], revenue = Revenue.objects.create(payment_type, quantity), discounts = Discounts.objects.create(member = quantity*(member_percentage + line_item_member_percentage - member_percentage*line_item_member_percentage - line_item_other_percentage*member_percentage), other = quantity*(other_percentage + line_item_other_percentage - other_percentage*line_item_other_percentage - line_item_member_percentage*other_percentage))) 

