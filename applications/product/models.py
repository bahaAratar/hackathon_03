from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    image = models.ImageField()
    price = models.IntegerField()

class Category(models.Model):
    stern = models.CharField(max_length=200) #кормы
    toys = models.CharField(max_length=200) #игрушки
