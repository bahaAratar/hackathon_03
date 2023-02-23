

from django.shortcuts import render,redirect
from rest_framework import viewsets
from .models import Contact,Delivery
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import ContactSerializer, DeliverySerializer
from rest_framework.decorators import action


class ContactViewSet(viewsets.ModelViewSet): # post , get
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
class DeliveryViewSet(viewsets.ModelViewSet):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    