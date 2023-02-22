from django.shortcuts import render
from rest_framework import generics
from .models import Card
from .serializers import CardSerializer

class CardList(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class =CardSerializer

class CardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

class CardCreate(generics.CreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

class CardUpdate(generics.UpdateAPIView):
    queryset = Card.objects.all()
    serializer_class =CardSerializer
