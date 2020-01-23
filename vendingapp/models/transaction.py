from django.db import models
from .vending import VendingMachine
from .coin import Coin


class Transaction(models.Model):
    vending_machine = models.ForeignKey("VendingMachine", on_delete=models.CASCADE)


 @property total_coins(self):
    total_coin = Coin.objects.filter(Transaction=self)
    transaction_total
    for x in total_coin
    transaction_total += total_coin.amount
    return transaction_total
