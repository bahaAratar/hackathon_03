from django.db import models


User = get_user_model()

class Product(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
 )
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.IntegerField()

class Category(models.Model):
    stern = models.CharField(unique=True, max_length=200) #кормы
    toys = models.CharField(unique=True, max_length=200) #игрушки
