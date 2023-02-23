from django.urls import path,include
from . import views
from .views import ContactViewSet ,DeliveryViewSet
from rest_framework.routers import DefaultRouter
 


router = DefaultRouter()
router.register('contacts', ContactViewSet)
router.register('delivery', DeliveryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
]
