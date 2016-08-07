from __future__ import unicode_literals

from django.db import models

from BSFC.apps.cost.models import Cost

# Create your models here.


class Item(models):
    """Model to describe an item"""
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
    
