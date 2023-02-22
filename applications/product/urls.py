from django.urls import path
from applications.product.views import ProductModelViewSet, CreateImageAPIView

urlpatterns = [
    path('tag/<slug:tag_slug>/',ProductModelViewSet.product_list, name='product_list_by_tag'),
    path('add/image/', CreateImageAPIView.as_view())
]