from rest_framework import serializers
from ..models.entities import Product

# Serializer of product model
class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

# Serializer for initial details
class InitialProductDetailSerializers(serializers.Serializer):
    Username = serializers.CharField()
    Product_Name = serializers.CharField()
    Product_Category = serializers.CharField()
    Product_Description = serializers.CharField()
        