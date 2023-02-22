from django.conf import settings
from django.db import models
from ..account.models import MyUser
from applications.product.models import Product

class Order(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"
