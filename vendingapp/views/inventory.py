"""View module for handling requests about inventory"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from vendingapp.models import Inventory


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
        """
        Handle GET requests for inventory
        Gets a single Inventory item

        """
        try:
            inventory = Inventory.objects.get(pk=pk)
            serializer = InventorySerializer(
                inventory, context={'request': request})
            return Response(serializer.data)

        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """
        GET all
        List out all of different inventory in the machine
        """
        inventory = Inventory.objects.all()

        serializer = InventorySerializer(
            inventory, many=True, context={'request': request})

        return Response(serializer.data, status=200)

    def update(self, request, pk=None):
        """
        Handle PUT requests for inventory
        Response -- HTTP_204_NO_CONTENT
        """
        inventory = Inventory.objects.get(pk=pk)
        # checks if the less then 2 coin are inserted and if their are still items in the inventory
        if inventory.vending_machine.coin >= 2 and inventory.quantity > 0:
            inventory.quantity = inventory.quantity-1
            inventory.save()
            http_code = status.HTTP_204_NO_CONTENT
            items_vended = 5-inventory.quantity
            headers = {"X-Inventory": inventory.quantity,
                       "X-coin": inventory.vending_machine.coin-2}
         # manages if less than 2 coin are inserted into the vending machine
        elif inventory.vending_machine.coin < 2:
            items_vended = 0
            http_code = status.HTTP_403_FORBIDDEN
            headers = {"X-coin": inventory.vending_machine.coin}
        # it sends up an error if inventory runs out
        elif inventory.quantity >= 0:
            items_vended = 0
            http_code = status.HTTP_404_NOT_FOUND
            headers = {"X-coin": inventory.vending_machine.coin}

        return Response({"quantity": items_vended}, status=http_code, headers=headers)
