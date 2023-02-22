from django.db import models

class Product(models.Model):
    name = models.CharField(unique=True, max_length=200)
    description = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True)
    price = models.IntegerField()

class Category(models.Model):
    stern = models.CharField(unique=True, max_length=200) #кормы
    toys = models.CharField(unique=True, max_length=200) #игрушки
