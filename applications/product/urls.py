from django.urls import path, include
from rest_framework.routers import DefaultRouter
from applications.product.views import ProductModelViewSet, CreateImageAPIView
from .views import *

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('categoryes', CategorytViewSet)

urlpatterns = [
    path('', include(router.urls)), 
    path('tag/<slug:tag_slug>/',ProductModelViewSet.product_list, name='product_list_by_tag'),
    path('add/image/', CreateImageAPIView.as_view())
]
