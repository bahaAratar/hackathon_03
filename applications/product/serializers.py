from rest_framework import serializers
from .models import *

class ProductImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductImage 
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    
    class Meta:
        model = Product
        fields = '__all__'
    def create(self, validated_data):
        product = Product.objects.create(**validated_data)
        request = self.context.get('request')
        data = request.FILES
        image_objects = []
        for i in data.getlist('images'):
            image_objects.append(ProductImage(product=product,image=i))
        ProductImage.objects.bulk_create(image_objects)

        return product
    
    # def to_representation(self, instance):
    #     representation =  super().to_representation(instance)

    #     representation['price'] = instance.likes.filter(is_like=True).count()
    #     for like in representation['likes']:
    #         representation['price'] = instance.ratings.all().aggregate(sum('price'))

    #     return representation
    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
