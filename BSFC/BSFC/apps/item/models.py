from __future__ import unicode_literals

from django.db import models

from BSFC.apps.cost.models import Cost
from BSFC.apps.item.constants import (
    FIXED, PER_UNIT,
    BAKERY,
    GROCERY,
    BULK,
    BSFC,
    PRODUCE,
    HEALTH_AND_BEAUTY,
    HOUSEHOLD,
    BEVERAGE,
    CHILL,
    GRAB_AND_GO,
    FROZEN
)

# Create your models here.


class Item(models.Model):
    """Model to describe an item"""
    price_type_choices = [
        (FIXED, 'fixed'),
        (PER_UNIT, 'per_unit')
    ]

    category_choices = [
        (BAKERY, "Bakery"),
        (GROCERY, "Grocery"),
        (BULK, "Bulk"),
        (BSFC, "BSFC"),
        (PRODUCE, "Produce"),
        (HEALTH_AND_BEAUTY, "Health & Beauty"),
        (HOUSEHOLD, "Household"),
        (BEVERAGE, "Beverage"),
        (CHILL, "Chill"),
        (GRAB_AND_GO, "Grab & Go"),
        (FROZEN, "Frozen")
    ]
    name = models.CharField(max_length=100,
                            null=True,
                            blank=True)
    description = models.TextField(null=True,
                                   blank=True)
    count = models.IntegerField()
    cost = models.OneToOneField(
        Cost,
        on_delete=models.CASCADE,
        primary_key=True
    )
    label = models.CharField(max_length=100,
                             null=True)
    price = models.FloatField()
    price_type = models.CharField(max_length=100,
                                  choices=price_type_choices,
                                  default=FIXED,
                                  null=True)
    unit_name = models.CharField(max_length=100,
                                 null=True)
    category = models.CharField(max_length=100,
                                choices=category_choices,
                                default=None,
                                null=True)

