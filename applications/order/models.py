from django.db import models
from ..product.models import *
from ..account.models import MyUser

class Order(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='myusers')
    items = models.TextField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)