from django.shortcuts import render
from rest_framework import generics, serializers
from .models import Product, ProductImage
from applications.product.serializers import ProductSerializer, ProductImageSerializer
from taggit.models import Tag
from django.shortcuts import get_object_or_404
from django.db.models import Count
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def product_detail(request, year, month, day, product):
        product = get_object_or_404(Product, slug=product, status='published',publish__year=year,
        publish__month=month,publish__day=day)
        product_tags_ids = product.tags.values_list('id', flat=True)
        similar_products = Product.objects.filter(tags__in=product_tags_ids).exclude(id=product.id)
        similar_products = similar_products.annotate(same_tags=Count('tags')).order_by('-same_tags','-publish')[:4]
        return render(request,'blog/post/detail.html',{'product': product})

    def product_list(request, tag_slug=None):
        object_list = Product.objects.all()
        tag = None
        if tag_slug:
            tag = get_object_or_404(Tag, slug=tag_slug)
            object_list = object_list.filter(tags__in=[tag])
        return render(request, 'product/list.html', {'products': object_list})
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['owner', 'name', 'price', 'status']
    search_fields = ['product']
    ordering_fields = ['id']
    
class CreateImageAPIView(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    permission_classes = [IsAuthenticated]

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class CategorytViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

