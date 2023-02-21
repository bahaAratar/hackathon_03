from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

# class DeliveryAddressSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DeliveryAddress
#         fields = '__all__'