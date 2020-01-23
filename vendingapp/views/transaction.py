from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import api_view
from vendingapp.models.transaction import Transaction
from vendingapp.views.coin import CoinSerializer

class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    # coins_accepted = CoinSerializer(many="True")
    class Meta:
        model = Transaction
        url = serializers.HyperlinkedIdentityField(
            view_name='transaction',
            lookup_field='id'
        )
        fields = ('id', 'coins_accepted', 'coins_accepted', 'foo')
        depth = 1

class TransactionView(ViewSet):
    queryset = Transaction.objects.all()
    def retrieve(self, request, pk=None):
        """Handle GET requests for transaction
        """
        try:
            transaction = Transaction.objects.get(pk=pk)
            serializer = TransactionSerializer(transaction, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
    def list(self, request):
        transaction = Transaction.objects.all()
        serializer = TransactionSerializer(
            transaction, many=True, context={'request': request})
        return Response(serializer.data)

        