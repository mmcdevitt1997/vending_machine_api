from django.db import models
class VendingMachine(models.Model):
    coin = models.IntegerField(default=0)
