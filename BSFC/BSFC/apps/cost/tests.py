from django.test import TestCase
from .models import Cost
from BSFC.apps.item.models import Item
from BSFC.apps.revenue.models import Revenue
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
            Item.objects.create(name='Apple', cost=self.costs[0], price=15, revenue=Revenue.objects.create(sold=1)),
            Item.objects.create(name='Orange', cost=self.costs[1], price=25, revenue=Revenue.objects.create(sold=1)),
            Item.objects.create(name='Pear', cost=self.costs[2], price=35, revenue=Revenue.objects.create(sold=1))
        ]
        today = datetime.today()
        self.start_date = datetime(today.year, today.month, today.day, 0, 0, 0, 0)
        self.end_date = datetime(today.year, today.month, today.day, 23, 59, 59, 999999)

    def test_all_cogs(self):
        all_cogs_expected = all_calculations.all_cogs(self.start_date, self.end_date)
        all_cogs = 0
        for item in self.items:
            all_cogs += item.revenue.sold * item.cost.item_cost
        self.assertEquals(all_cogs_expected, all_cogs)
