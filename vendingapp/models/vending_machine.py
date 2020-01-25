from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from .inventory import Inventory


class VendingMachine(models.Model):
    coin = models.IntegerField(default=0)


@receiver(post_save, sender=VendingMachine)
def stock_vending_machine(instance, created, **kwargs):
    items = 3
    if created:
        for item_amount in range(0, items):
            Inventory.objects.create(
                quantity=5,
                vending_machine=instance
            )
