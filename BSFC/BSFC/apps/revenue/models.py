from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Revenue(models.Model):
    """Model for fields to take off revenue calc"""
    store_use = models.FloatField(null=True,
                                  default=0.0)
    spoilage = models.FloatField(null=True,
                                 default=0.0)
    food_prep = models.FloatField(null=True,
                                  default=0.0)
    committee = models.FloatField(null=True,
                                  default=0.0)

    def __str__(self):
        return ' | '.join([
            str(self.store_use),
            str(self.spoilage),
            str(self.food_prep),
            str(self.committee)
        ])
