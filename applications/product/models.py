from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth import get_user_model
from django.utils import timezone


User = get_user_model()

class Product(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
 )
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    slug = models.SlugField(max_length=250)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    tags = TaggableManager()
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    
    class Meta:
        ordering = ('-published',)
    
    def __str__(self):
        return self.name
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='post_images')

    def __str__(self) -> str:
        return f'{self.product.name}'


class Category(models.Model):
    stern = models.CharField(max_length=200) #кормы
    toys = models.CharField(max_length=200) #игрушки
