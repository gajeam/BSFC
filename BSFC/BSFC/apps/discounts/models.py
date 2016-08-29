from __future__ import unicode_literals

from django.db import models

class Discounts(models.Model):
    """Model to describe quantity of the item subject to discounts"""
    member = models.FloatField(null=True,
                                  default=0.0)
    other = models.FloatField(null=True,
                                  default=0.0)

    def update_discounts(quantity, is_member):
    	if is_member:
    		self.member += quantity
    	else:
    		self.other += quantity

    	self.save()

    def get_discounts(member_only):
    	if get_member:
    		return self.member
    	else:
    		return self.member + self.other

    def __str__(self):
        return ' | '.join([
            str(self.member),
            str(self.other)
        ])