from django.db import models

class Candle(models.Model):
    id = models.IntegerField()
    open = models.DecimalField(max_digits=12, decimal_places=6)
    high = models.DecimalField(max_digits=12, decimal_places=6)
    low = models.DecimalField(max_digits=12, decimal_places=6)
    close = models.DecimalField(max_digits=12, decimal_places=6)
    date = models.DateTimeField()

