from django.urls import path, include
from .views import CardViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('cards', CardViewSet)

urlpatterns = [
    path('', include(router.urls)), 
]
