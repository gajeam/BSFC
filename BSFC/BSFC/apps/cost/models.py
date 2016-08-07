from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Cost(models.Model):
    """Model to describe the cost of an item"""
    item_cost = models.FloatField()

    def __str__(self):
        return str(self.item_cost)



