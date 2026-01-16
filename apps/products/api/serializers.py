from rest_framework import serializers
from ..models.entities import Product

# Serializer of product model
class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        