from rest_framework import serializers
from apps.products.models.entities import Product
from apps.products.services.create import product

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
    def create(self, validated_data):
        product_available = product(validated_data)
        return product_available