# from django.http import HttpResponseServerError
# from rest_framework.viewsets import ViewSet
# from rest_framework.response import Response
# from rest_framework import serializers
# from rest_framework import status
# from vendingapp.models.coin import Coin

# class CoinSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Coin
#         url = serializers.HyperlinkedIdentityField(
#             view_name='coin',
#             lookup_field='id'
#         )
#         fields = ('id', 'coin')
#         depth = 1

