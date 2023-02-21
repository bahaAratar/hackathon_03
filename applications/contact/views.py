from django.shortcuts import render
from rest_framework import generics
from .models import Contact
from .serializers import ContactSerializer

class ContactList(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

# class DeliveryAddressList(generics.ListAPIView):
#     queryset = DeliveryAddress.objects.all()
#     serializer_class = DeliveryAddressSerializer

class ContactCreate(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

# class DeliveryAddressCreate(generics.CreateAPIView):
#     queryset = DeliveryAddress.objects.all()
#     serializer_class = DeliveryAddressSerializer

class ContactUpdate(generics.RetrieveUpdateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

# class DeliveryAddressUpdate(generics.RetrieveUpdateAPIView):
#     queryset = DeliveryAddress.objects.all()
#     serializer_class = DeliveryAddressSerializer

class ContactDelite(generics.DestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer