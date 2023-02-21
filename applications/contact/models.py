from django.db import models

class Contact(models.Model):
    address = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=200)
    instagram = models.URLField()
    telegram = models.URLField()

# class DeliveryAddress(models.Model):
#     name = models.CharField(max_length=255)
#     address = models.CharField(max_length=255)
#     phone = models.CharField(max_length=20)