from .inventory import Inventory
from .transaction import Transaction

class InventoryTransaction(models.Model):
   inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
   transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)

