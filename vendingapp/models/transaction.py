from django.db import models
from .vending import VendingMachine
from .coin import Coin


class Transaction(models.Model):
    vending_machine = models.ForeignKey("VendingMachine", on_delete=models.CASCADE)


    class Meta:
        verbose_name = ("transaction")
        verbose_name_plural = ("transaction")

    @property
    def coins_accepted(self):
        total_coin = Coin.objects.filter(transaction=self)
        transaction_total = 0
        for coin in total_coin:
            transaction_total += coin.amount
        return transaction_total

    @property
    def coins_returned(self):
        coins_returned = self.coins_accepted - 2
        return coins_returned

    @property
    def foo(self):
        return "foo"
