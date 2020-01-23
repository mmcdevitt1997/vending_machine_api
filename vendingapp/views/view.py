# from django.http import HttpResponseServerError
# from rest_framework.viewsets import ViewSet
# from rest_framework.response import Response
# from rest_framework import serializers
# from rest_framework import status
# from rest_framework.decorators import api_view
# from vendingapp.views.coin import CoinSerializer
# from vendingapp.models.coin import Coin

# @api_view(['PUT', 'DELETE '])
# def coin_view(request, slug):
#     if request.method == 'PUT':
#         serializer = CoinSerializer(coin, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_204 ,headers="1 of coins accepted"  )
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# if request.method == 'DELETE' and Coin :
#          Coin.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

