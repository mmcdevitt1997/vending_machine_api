from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from vendingapp.models import *
from vendingapp.views import *

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'inventory', InventoryView, 'Inventory')
router.register(r'users', Users, 'User')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-token-auth/', obtain_auth_token),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^register$', register_user),
    url(r'^login$', login_user),
]
