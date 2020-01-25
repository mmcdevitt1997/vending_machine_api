from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from vendingapp.models import *
from vendingapp.views import *

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'inventory', InventoryView, 'Inventory')
router.register(r'', VendingMachineView, '')


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
