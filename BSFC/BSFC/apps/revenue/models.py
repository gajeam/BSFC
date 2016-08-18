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
    sold = models.FloatField(null=True,
                             default=0.0)

    def update_revenue_field(field_key, amount):
      if field_key == STORE_USE
        self.store_use += amount
      elif field_key == SPOILAGE
        self.spoilage += amount
      elif field_key == FOOD_PREP
        self.food_prep += amount
      elif field_key == COMMITTEE
        self.committee += amount
      else
        self.sold += amount

      self.save()

    def get_revenue_field(field_key):
      if field_key == STORE_USE
        return self.store_use
      elif field_key == SPOILAGE
        return self.spoilage
      elif field_key == FOOD_PREP
        return self.food_prep
      elif field_key == COMMITTEE
        return self.committee
      else
        return self.sold


    def __str__(self):
        return ' | '.join([
            str(self.store_use),
            str(self.spoilage),
            str(self.food_prep),
            str(self.committee),
            str(self.sold)
        ])
