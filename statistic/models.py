from django.db import models


class Event(models.Model):
    date = models.DateField()
    views = models.DecimalField(decimal_places=0,
                                max_digits=10,
                                default=0)
    clicks = models.DecimalField(decimal_places=0,
                                 max_digits=10,
                                 default=0)
    cost = models.DecimalField(decimal_places=2,
                               max_digits=10,
                               default=0)
