from django.db import models
from applications.product.models import Product
from django.contrib.auth import get_user_model

User = get_user_model()

class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.owner} -> {self.product.name}'


class Rating(models.Model):
    RATING = (
        ('1', 'очень плохо'),
        ('2', 'плохо'),
        ('3', 'нормально'),
        ('4', 'хорошо'),
        ('5', 'отлично')
    )
    rating = models.CharField(max_length=50, choices=RATING)
    product = models.ForeignKey(Product, related_name='rating', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='rating', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.user} --> {self.product.name}'