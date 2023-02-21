from django.shortcuts import render
from rest_framework import generics
from .models import Product
from serializers import ProductSerializer

class ContacttList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ContactCreate(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ContactUpdate(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer