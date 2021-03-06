"""View module for handling requests about Vending Machine"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from vendingapp.models.vending_machine import VendingMachine
from vendingapp.views.inventory import InventorySerializer


class VendingMachineSerializer(serializers.HyperlinkedModelSerializer):

    inventory = InventorySerializer(many="True")
    class Meta:
        model = VendingMachine
        url = serializers.HyperlinkedIdentityField(
            view_name='VendingMachine',
            lookup_field='id'
        )
        fields = ('id', 'quantity', 'coin')
        depth = 1


class VendingMachineView(ViewSet):
    queryset = VendingMachine.objects.all()

    def update(self, request, pk=None):
        """
            Handle PUT requests for coins
            Response -- 204 status code

         """
        vending_machine = VendingMachine.objects.get(pk=pk)
        vending_machine.coin = request.data["coin"]
        headers = {
            "X-Coins": vending_machine.coin
        }
        vending_machine.save()
        return Response({}, status=status.HTTP_204_NO_CONTENT, headers=headers)

    def destroy(self, request, pk=None):
        """
      Handle DELETE requests for a for the coins so that you can tell
      how much change is going back to the customer

        Returns:
            Response -- 204, 404, or 500 status code
        """
        try:
            vending_machine = VendingMachine.objects.get(pk=pk)
            vending_machine.coin = request.data["coin"]
            headers = {"X-Coins": vending_machine.coin-2}

            return Response({}, status=status.HTTP_204_NO_CONTENT, headers=headers)

        except VendingMachine.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
