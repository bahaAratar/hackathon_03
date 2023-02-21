from django.db import models

from django.db import models
from ..account.models import MyUser
from ..product.models import Product

class Card(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='users')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')