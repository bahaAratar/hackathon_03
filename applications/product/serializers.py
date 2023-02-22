from rest_framework import serializers
from .models import Product, ProductImage

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
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
