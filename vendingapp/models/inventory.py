from django.db import models

class Inventory(models.Model):
    quantity = models.IntegerField(default=5)
    vending_machine = models.ForeignKey("VendingMachine", on_delete=models.CASCADE)

