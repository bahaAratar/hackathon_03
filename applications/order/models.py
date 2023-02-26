from django.db import models
from ..product.models import *
from ..account.models import MyUser
from django.contrib.auth import get_user_model
import uuid

User = get_user_model()

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='myusers', blank=True)
    items = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'order/history'
        verbose_name = 'заказ/история'
        verbose_name_plural = 'заказы/истории'