from django.shortcuts import render
from rest_framework import generics
from .models import Card
from .serializers import CardSerializer

class ContactList(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class =CardSerializer

class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer