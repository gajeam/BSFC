from django.test import TestCase
from BSFC.apps.cost.models import Cost
from .models import Item
from BSFC.apps.revenue.models import Revenue
from BSFC.public import all_calculations, item_calculations
from datetime import datetime


class ItemFilteringTests(TestCase):
    def setUp(self):
        self.costs = [
            Cost.objects.create(item_cost=10) for _ in range(3)
        ]
        self.items = [
            Item.objects.create(name='Apple', cost=self.costs[0], price=10, revenue=Revenue.objects.create(sold=1)),
            Item.objects.create(name='Orange', cost=self.costs[1], price=10, revenue=Revenue.objects.create(sold=1)),
            Item.objects.create(name='Pear', cost=self.costs[2], price=10, revenue=Revenue.objects.create(sold=1))
        ]
        self.date1 = datetime(2015, 10, 10, 0, 0, 0, 0)
        self.date2 = datetime(2015, 10, 11, 0, 0, 0, 0)
        self.date3 = datetime(2015, 10, 12, 0, 0, 0, 0)
        self.bad_date1 = datetime(2015, 10, 8, 0, 0, 0, 0)
        self.bad_date2 = datetime(2015, 10, 9, 0, 0, 0, 0)
        self.items[0].created_at = self.date1
        self.items[0].save()
        self.items[1].created_at = self.date2
        self.items[1].save()
        self.items[2].created_at = self.date3
        self.items[2].save()

    def test_no_items_available(self):
        qs = all_calculations.get_items_between_dates(self.bad_date1, self.bad_date2)
        self.assertFalse(qs.exists())

    def test_no_items_available_by_name(self):
        qs = item_calculations.get_items_between_dates_by_name('Banana', self.date1, self.date3)
        self.assertFalse(qs.exists())

    def test_one_item_available(self):
        qs = all_calculations.get_items_between_dates(self.date1, self.date1)
        self.assertListEqual(list(qs), [self.items[0]])

    def test_one_item_available_by_name(self):
        qs = item_calculations.get_items_between_dates_by_name('Apple', self.bad_date2, self.date1)
        self.assertListEqual(list(qs), [self.items[0]])

    def test_all_items_available(self):
        qs = all_calculations.get_items_between_dates(self.date1, self.date3)
        self.assertListEqual(list(qs), self.items)
