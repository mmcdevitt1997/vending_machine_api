from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from vendingapp.models import Inventory


class InventorySerializer(serializers.HyperlinkedModelSerializer):
    lass Meta:
        model = Inventory
        url = serializers.HyperlinkedIdentityField(
            view_name='Inventory',
            lookup_field='id'
        )
        fields = ('id', 'vending_machine', 'amount' )

