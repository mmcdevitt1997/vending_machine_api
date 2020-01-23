from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import api_view
from vendingapp.models.inventory import Inventory

class InventorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Inventory
        url = serializers.HyperlinkedIdentityField(
            view_name='inventory',
            lookup_field='id'
        )
        fields = ('id', 'quantity', 'vending_machine')


class InventoryView(ViewSet):
    queryset = Inventory.objects.all()
    def retrieve(self, request, pk=None):
        """Handle GET requests for inventory
        """
        try:
            inventory = Inventory.objects.get(pk=pk)
            serializer = InventorySerializer(inventory, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
    def list(self, request):

        inventory = Inventory.objects.all()
        serializer = InventorySerializer(
            inventory, many=True, context={'request': request})
        return Response(serializer.data)

@api_view (['PUT'])
def put_inventory(request, pk):
    try:
        inventory = Inventory.objects.get(pk=pk)
    except Inventory.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = InventorySerializer(inventory, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
