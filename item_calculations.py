from BSFC.apps.item.models import Item
from BSFC.apps.cost.models import Cost
from BSFC.apps.revenue.models import Revenue
from BSFC.apps.revenue.constants import (
    tender_choices
)


def get_items_between_dates_by_name(name, start_date, end_date):
    return Item.objects.filter(name=name, created_at__gte=start_date, created_at__lte=end_date)


def item_revenue(name, start_date, end_date):
    item_qs = get_items_between_dates_by_name(name, start_date, end_date)
    total_revenue = 0
    for item in item_qs:
        price = item.price #included in for loop to account for changing prices over time
        total_revenue += item.revenue.get_revenue_field(tender_choices['SOLD'])*price #minus refunds, discounts
    return total_revenue


def item_cogs(name, start_date, end_date):
    item_qs = get_items_between_dates_by_name(name, start_date, end_date)
    total_cogs = 0
    for item in item_qs:
        cost = item.cost.item_cost #included in for loop to account for changing costs over time
        total_cogs += item.revenue.get_revenue_field(tender_choices['SOLD'])*cost
    return total_cogs


def item_losses(name, start_date, end_date, field_key):
    item_qs = get_items_between_dates_by_name(name, start_date, end_date)
    total_losses = 0
    for item in item_qs:
        cost = item.cost.item_cost #included in for loop to account for changing costs over time
        total_losses += item.revenue.get_revenue_field(field_key)*cost
    return total_losses


def item_profit(name, start_date, end_date):
    item_losses = 0
    item_qs = get_items_between_dates_by_name(name, start_date, end_date)

    for item in item_qs:
        item_losses += sum([item.revenue.get_revenue_field(key) for key in tender_choices if key != 'SOLD'])
    return item_revenue(name, start_date, end_date) - item_cogs(name, start_date, end_date) - item_losses
