from BSFC.apps.item.models import Item
from BSFC.apps.cost.models import Cost
from BSFC.apps.revenue.models import Revenue
from BSFC.apps.revenue.constants import (
	tender_choices
	)
from item_calculations import (
	item_revenue, item_cogs, item_losses, item_profit
)


def all_revenue(start_date, end_date):
	item_qs = Item.objects.filter(created_at > start_date, created_at < end_date)
	total_revenue = 0
	for item in item_qs:
		total_revenue += item_revenue(item.name, start_date, end_date)
	return total_revenue

def all_cogs(start_date, end_date):
	item_qs = Item.objects.filter(created_at > start_date, created_at < end_date)
	total_cogs = 0
	for item in item_qs:
		total_cogs += item_cogs(item.name, start_date, end_date)
	return total_cogs

def all_losses(start_date, end_date, field_key):
	item_qs = Item.objects.filter(created_at > start_date, created_at < end_date)
	total_losses = 0
	for item in item_qs:
		total_losses += item_losses(item.name, start_date, end_date, field_key)
	return total_losses

def all_profit(start_date, end_date):
	item_qs = Item.objects.filter(created_at > start_date, created_at < end_date)
	total_profit = 0
	for item in item_qs:
		total_profit += item_profit(item.name, start_date, end_date)
	return total_profit