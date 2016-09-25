from django.test import TestCase
from BSFC.apps.cost.models import Cost
from BSFC.apps.item.models import Item
from BSFC.apps.revenue.models import Revenue
from BSFC.apps.revenue.constants import tender_choices
from BSFC.public import all_calculations
from datetime import datetime


class TestCostOfGoodsSold(TestCase):
    def setUp(self):
        self.costs = [
            Cost.objects.create(item_cost=10),
            Cost.objects.create(item_cost=20),
            Cost.objects.create(item_cost=30)
        ]
        self.items = [
            Item.objects.create(name='Apple', cost=self.costs[0], price=15, revenue=Revenue.objects.create(sold=3, committee=1, spoilage=1)),
            Item.objects.create(name='Orange', cost=self.costs[1], price=25, revenue=Revenue.objects.create(sold=7, spoilage=1, store_use=2)),
            Item.objects.create(name='Pear', cost=self.costs[2], price=35, revenue=Revenue.objects.create(sold=1, food_prep=1))
        ]
        today = datetime.today()
        self.start_date = datetime(today.year, today.month, today.day, 0, 0, 0, 0)
        self.end_date = datetime(today.year, today.month, today.day, 23, 59, 59, 999999)

    def test_all_revenue(self):
        all_revenue_expected = all_calculations.all_revenue(self.start_date, self.end_date)
        all_revenue = 0
        for item in self.items:
            all_revenue += item.revenue.sold * item.price
        self.assertEquals(all_revenue_expected, all_revenue)

    def test_all_losses(self):
    	all_losses_expected = 0
    	all_losses = 0
    	for key in tender_choices:
    		all_losses_expected += all_calculations.all_losses(self.start_date, self.end_date, key)
    		for item in self.items:
    			all_losses += item.revenue.get_revenue_field(key) * item.cost.item_cost
    	self.assertEquals(all_losses_expected, all_losses)

    def test_all_profit(self):
    	all_profit_expected = all_calculations.all_profit(self.start_date, self.end_date)
    	all_profit = 0
    	for item in self.items:
    		all_profit += item.revenue.sold * (item.price - item.cost.item_cost)
    		for key in ['STORE_USE', 'FOOD_PREP', 'SPOILAGE', 'COMMITTEE']:
    			all_profit -= item.revenue.get_revenue_field(tender_choices[key]) * item.cost.item_cost
    	self.assertEquals(all_profit_expected, all_profit)
