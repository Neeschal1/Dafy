from django.contrib.auth.models import User
from ..models.entities import Product
from ..api.serializers import ProductSerializers
from rest_framework.response import Response


def create_a_new_product(prod):

    product = Product.objects.create(
        Product_Name=prod.validated_data["Product_Name"],
        Product_Category=prod.validated_data["Product_Category"],
        Product_Description=prod.validated_data["Product_Description"],
        Image_one=prod.validated_data["Image_one"],
        Image_two=prod.validated_data["Image_two"],
        Image_three=prod.validated_data["Image_three"],
        Image_four=prod.validated_data["Image_four"],
        Image_five=prod.validated_data["Image_five"],
        Seller_Address=prod.validated_data["Seller_Address"],
        Price=prod.validated_data["Price"],
        Bought_Date=prod.validated_data["Bought_Date"],
        Seller_Name=prod.validated_data["Seller_Name"],
    )

    user_product = ProductSerializers(product)
    user = product.Seller_Name

    return Response(
        {
            "Message": "Product successfully created",
            "Seller's Detail": {
                "Full Name": user.first_name,
                "Username": user.username,
                "Email": user.email,
            },
            "Data": user_product.data,
        }
    )
