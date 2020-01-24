# from django.http import HttpResponseServerError
# from rest_framework.viewsets import ViewSet
# from rest_framework.response import Response
# from rest_framework import serializers
# from rest_framework import status
# from rest_framework.decorators import api_view
# from vendingapp.models.coin import Coin
# class CoinSerializer(serializers.HyperlinkedModelSerializer):
#     # transaction = TransactionSerializer(many="True")
#     class Meta:
#         model = Coin
#         url = serializers.HyperlinkedIdentityField(
#             view_name='coin',
#             lookup_field='id'
#         )
#         fields = ('id', 'coin')
#         depth = 2
# class CoinView(ViewSet):
    # queryset = Coin.objects.all()
    # def update(self, request, pk=None):
    #         """Handle PUT requests for foo
    #         Returns:
    #             Response -- Empty body with 204 status code
    #         """
    #         foo = Foo.objects.get(pk=pk)
    #         foo.<prop to update> = request.data["some property"]
    #         foo.save()
    #         return Response({}, status=status.HTTP_204_NO_CONTENT)

    # def update(self, request, pk=None):
    #     """Handle PUT requests for foo
    #          Returns:
    #          Response -- Empty body with 204 status code
    #          """
    #     coin = Coin.objects.get(pk=pk)
    #     coin.coin = request.data["coin"]
    #     if coin.coin <= 2:

    #     coin.save()
    #     return Response({}, status=status.HTTP_204_NO_CONTENT)



