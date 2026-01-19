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
    
    
# Serializer for images details
class ProductImagesDetailSerializers(serializers.Serializer):
    Username = serializers.CharField()
    Image_one = serializers.URLField(allow_blank = False)
    Image_two = serializers.URLField(allow_blank = False)
    Image_three = serializers.URLField(allow_blank = False)
    Image_four = serializers.URLField(required = False, allow_blank = True)
    Image_five = serializers.URLField(required = False, allow_blank = True)
        

# Serializer for Seller's detail
class ProductSellerDetailSerializers(serializers.Serializer):
    Username = serializers.CharField()
    Selling_Price = serializers.IntegerField()
    Estimated_Bought_Date = serializers.DateTimeField()