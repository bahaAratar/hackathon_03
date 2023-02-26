# from rest_framework import serializers
# from .models import Order

# class OrderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Order
#         fields = '__all__'

from rest_framework import serializers
from .models import Order
from ..product.models import Product

class OrderSerializer(serializers.ModelSerializer):
    items = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), many=True)
    total_price = serializers.DecimalField(read_only=True, max_digits=10, decimal_places=2)

    class Meta:
        model = Order
        fields = ['user', 'items', 'total_price']

    def create(self, validated_data):
        items = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        total_price = 0
        for item in items:
            total_price += item.price
            order.items.add(item)
        order.total_price = total_price
        order.save()
        return order
