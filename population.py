from BSFC.apps.item.models import Item
from BSFC.apps.cost.models import Cost
from BSFC.apps.revenue.models import Revenue

def create_todays_items():
	"""create Item object for each item in Clover inventory on the day called"""
	todays_inventory = #call to REST API to get list of all items, expanding by 'categories' and filering by day

	for item_dict in todays_inventory:
		Items.objects.create(name = item_dict['name'], cost = Cost.objects.create(item_cost = item_dict['cost']), price = item_dict['price'], price_type = item_dict['priceType'], unit_name = item_dict['unitName'] if 'unitName' in item_dict else None, category = item_dict['categories']['elements'][0]['name'], revenue = Revenue.objects.create())

def update_todays_items():
	"""use payments from the day to record quantity of each item contributing to revenue calculation"""
	todays_payments = #call to REST API to get list of all payments, expanding by 'order,' 'refunds,' and 'tender' and filtering by day

	for payment_dict in todays_payments:
		member_disc = False
		other_disc = False
		todays_date = #whatever convention we are using for dates...?
		payment_type = payment_dict['tender']['label']
		order_dict = #get corresponding order with payment['order']['id'], expanding by 'lineItems,' 'discounts'
		if 'discounts' in order_dict:
			if order_dict['discounts']['name'] == 'Member': #?
				member_disc = True
			elif 'percentage' in order_dict['discounts']:
				other_disc = True
			else:
				Discount.objects.create(other = order_dict['discounts']['amount'])
		for line_item_dict in order_dict['lineItems']['elements']:
			Item.objects.get(name = line_item_dict['name'], created_at.date() = todays_date).revenue.update_revenue_field(payment_type, item.quantity)  
			if member_disc:
				Item.objects.get(name = line_item_dict['name'], created_at.date() = todays_date).discounts.update_discounts(item.quantity, True)
			elif other_disc:
				Item.objects.get(name = line_item_dict['name'], created_at.date() = todays_date).discounts.update_discounts(item.quantity, False)

