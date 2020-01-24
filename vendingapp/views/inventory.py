from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import api_view
from vendingapp.models import Inventory, VendingMachine


class InventorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Inventory
        url = serializers.HyperlinkedIdentityField(
            view_name='inventory',
            lookup_field='id'
        )
        fields = ('id', 'quantity')
        depth = 2


class InventoryView(ViewSet):
    queryset = Inventory.objects.all()

    def retrieve(self, request, pk=None):
        """Handle GET requests for inventory
        """
        try:
            inventory = Inventory.objects.get(pk=pk)
            serializer = InventorySerializer(
                inventory, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):

        inventory = Inventory.objects.all()
        serializer = InventorySerializer(
            inventory, many=True, context={'request': request})
        return Response(serializer.data, status=200)

    def update(self, request, pk=None):
        """Handle PUT requests for coins
             Returns:
             Response -- Empty body with 204 status code
             """

        inventoryobject = Inventory.objects.get(pk=pk)
        if inventoryobject.vending_machine.coin >= 2 and inventoryobject.quantity > 0:
            inventory = Inventory.objects.get(pk=pk)
            inventory.quantity = inventoryobject.quantity-1
            inventory.save()
            http_code = status.HTTP_204_NO_CONTENT
            items_vended = 5-inventoryobject.quantity
            headers = {"X-Inventory": inventory.quantity,
                       "X-coin": inventory.vending_machine.coin-2}
        elif inventoryobject.vending_machine.coin < 2:
            items_vended = 0
            http_code = status.HTTP_403_FORBIDDEN
            headers = {"X-coin": inventoryobject.vending_machine.coin}
        elif inventoryobject.quantity >= 0:
            items_vended = 0
            http_code = status.HTTP_404_NOT_FOUND
            headers = {"X-coin": inventoryobject.vending_machine.coin}
        return Response({"quantity": items_vended}, status=http_code, headers=headers)
