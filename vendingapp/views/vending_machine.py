from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import api_view
from vendingapp.models.vending_machine import VendingMachine


class CoinSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VendingMachine
        url = serializers.HyperlinkedIdentityField(
            view_name='VendingMachine',
            lookup_field='id'
        )
        fields = ('id', 'coin')
        depth = 1


class VendingMachineView(ViewSet):
    queryset = VendingMachine.objects.all()

    def update(self, request, pk=None):
        """Handle PUT requests for coins
             Returns:
             Response -- Empty body with 204 status code
             """
        vending_machine = VendingMachine.objects.get(pk=pk)
        vending_machine.coin = request.data["coin"]
        headers = {
            "X-Coins": vending_machine.coin
        }
        vending_machine.save()
        return Response({}, status=status.HTTP_204_NO_CONTENT, headers=headers)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single park area

        Returns:
            Response -- 200, 404, or 500 status code
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
