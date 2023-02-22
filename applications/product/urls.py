from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('categoryes', CategorytViewSet)
router.register('image_add', CreateImageAPIView)

urlpatterns = [
    path('', include(router.urls)), 
    # path('tag/<slug:tag_slug>/',ProductViewSet.product_list, name='product_list_by_tag'),
    # path('add/image/', CreateImageAPIView.as_view())
]
