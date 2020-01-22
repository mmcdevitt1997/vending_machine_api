from django.db import models
from .vending import VendingMachine

class Transaction(models.Model):
    vending_machine = models.ForeignKey("VendingMachine", on_delete=models.CASCADE)

