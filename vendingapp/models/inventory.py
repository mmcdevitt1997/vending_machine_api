from django.db import models
from .vending import VendingMachine

class Inventory(models.Model):
    amount = models.IntegerField(default=5)
    vending_machine = models.ForeignKey("VendingMachine", on_delete=models.CASCADE)