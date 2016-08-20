from BSFC.apps.item.models import Item
from BSFC.apps.cost.models import Cost
from BSFC.apps.revenue.models import Revenue
from BSFC.apps.revenue.constants import (
	tender_choices
	)


def all_revenue(name, start_date, end_date):
	item_qs = Item.objects.filter(name = name, created_at > start_date, created_at < end_date)
	total_revenue = 0
	for item in item_qs
		price = item.price #included in for loop to account for changing prices over time
		total_revenue += item.get_revenue_field(tender_choices['SOLD'])*price #minus refunds, discounts
	return total_revenue

def all_cogs(name, start_date, end_date):
	item_qs = Item.objects.filter(name = name, created_at > start_date, created_at < end_date)
	total_cogs = 0
	for item in item_qs
		cost = item.cost #included in for loop to account for changing costs over time
		total_cost += item.get_revenue_field(tender_choices['SOLD'])*cost
	return total_cogs

def all_losses(name, start_date, end_date, field_key)
	item_qs = Item.objects.filter(name = name, created_at > start_date, created_at < end_date)
	total_losses = 0
	for item in item_qs
		cost = item.cost #included in for loop to account for changing costs over time
		total_losses += item.get_revenue_field(field_key)*cost
	return total_losses

def all_profit(name, start_date, end_date):
	item_losses = 0
	for key in tender_choices
		if key != tender_choices['SOLD']
			item_losses += item.get_revenue_field(key)
	return item_revenue(name, start_date, end_date) - item_cogs(name, start_date, end_date) - item_losses