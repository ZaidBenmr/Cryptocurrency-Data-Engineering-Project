from django.urls import path, include
from bitcoin.views import BtcViewSet
from rest_framework import routers


app_name='bitcoin'

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'bitcoin', BtcViewSet)


urlpatterns = [
    
    path('', include(router.urls)),
    
]


