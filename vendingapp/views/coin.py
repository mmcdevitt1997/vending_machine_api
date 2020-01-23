from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import api_view
from vendingapp.models.coin import Coin
class CoinSerializer(serializers.HyperlinkedModelSerializer):
    # transaction = TransactionSerializer(many="True")
    class Meta:
        model = Coin
        url = serializers.HyperlinkedIdentityField(
            view_name='coin',
            lookup_field='id'
        )
        fields = ('id', 'coin', 'transaction')
        depth = 2
class CoinView(ViewSet):
    queryset = Coin.objects.all()
    def retrieve(self, request, pk=None):
        """Handle GET requests for coins
        """
        try:
            coin = Coin.objects.get(pk=pk)
            serializer = CoinSerializer(coin, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
    def list(self, request):
        coin = Coin.objects.all()
        serializer = CoinSerializer(
           coin, many=True, context={'request': request})
        return Response(serializer.data)