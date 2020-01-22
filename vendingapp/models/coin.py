from django.db import models
from .transaction import Transaction 

class Coin (models.Model):
    coin = models.IntegerField(default= 1)
    transaction = models.ForeignKey("Transaction", on_delete=models.CASCADE)
