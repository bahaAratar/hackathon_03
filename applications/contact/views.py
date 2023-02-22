

from django.shortcuts import render
from rest_framework import viewsets
from .models import Contact
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import ContactSerializer

class ContactViewSet(viewsets.ModelViewSet): # post , get
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

