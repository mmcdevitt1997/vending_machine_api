from django.db import models
class VendingMachine(models.Model):
    coin = models.IntegerField(defalt=0 )

    # @property
    # def coins_accepted(self):
    #     total_coin = Coin.objects.filter(transaction=self)
    #     transaction_total = 0
    #     for coin in total_coin:
    #         transaction_total += coin.amount
    #     return transaction_total

    # @property
    # def coins_returned(self):
    #     coins_returned = self.coins_accepted - 2
    #     return coins_returned