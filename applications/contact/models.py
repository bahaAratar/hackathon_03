from django.db import models

class Contact(models.Model):
    address = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=200)
    instagram = models.URLField()
    telegram = models.URLField()

class Delivery(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    address = models.CharField(max_length=200)
    