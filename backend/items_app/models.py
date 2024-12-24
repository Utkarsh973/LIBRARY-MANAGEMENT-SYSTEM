from django.db import models

class Item(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    