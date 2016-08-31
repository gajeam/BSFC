from __future__ import unicode_literals

from django.db import models

from django.utils import timezone

# Create your models here.

class Tips(models.Model):
	"""Model to store total donations ("tips") for a single day"""
	date = models.DateTimeField(auto_now_add=True)
	amount = models.FloatField(null=True,
                                  default=0.0)