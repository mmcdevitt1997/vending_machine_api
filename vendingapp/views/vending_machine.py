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
    #  def update(self, request, pk=None):
    #          """Handle PUT requests for foo
    #        Returns:
    #              Response -- Empty body with 204 status code
    #          """
    #          foo = Foo.objects.get(pk=pk)
    #         foo.<prop to update> = request.data["some property"]
    #          foo.save()
    #        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def update(self, request, pk=None):
        """Handle PUT requests for coins
             Returns:
             Response -- Empty body with 204 status code
             """
        coin = VendingMachine.objects.get(pk=pk)
        coin.coin = request.data["coin"]
        coin.save()
        return Response({}, status=status.HTTP_204_NO_CONTENT)

    # def destory(self, )


