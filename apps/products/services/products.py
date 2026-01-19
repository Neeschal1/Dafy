# from django.contrib.auth.models import User
# from ..models.entities import Product
# from ..api.serializers import ProductSerializers
# from rest_framework.response import Response


# def create_a_new_product(prod):

#     product = Product.objects.create(
#         Product_Name=prod.validated_data["Product_Name"],
#         Product_Category=prod.validated_data["Product_Category"],
#         Product_Description=prod.validated_data["Product_Description"],
#         Image_one=prod.validated_data["Image_one"],
#         Image_two=prod.validated_data["Image_two"],
#         Image_three=prod.validated_data["Image_three"],
#         Image_four=prod.validated_data["Image_four"],
#         Image_five=prod.validated_data["Image_five"],
#         Seller_Address=prod.validated_data["Seller_Address"],
#         Price=prod.validated_data["Price"],
#         Bought_Date=prod.validated_data["Bought_Date"],
#         Seller_Name=prod.validated_data["Seller_Name"],
#     )

#     user_product = ProductSerializers(product)
#     user = product.Seller_Name

#     return Response(
#         {
#             "Message": "Product successfully created",
#             "Seller's Detail": {
#                 "Full Name": user.first_name,
#                 "Username": user.username,
#                 "Email": user.email,
#             },
#             "Data": user_product.data,
#         }
#     )


from django.contrib.auth.models import User
from ..models.entities import Product
from ..api.serializers import ProductSerializers
from rest_framework.response import Response
from django.core.cache import cache

def create_a_new_product(username):
    product_detail = cache.get(username)
    image_detail = cache.get(f"images_{username}")
    seller_detail = cache.get(f"seller_detail_{username}")
    
    if not all([product_detail, image_detail, seller_detail]):
        return Response(
            {"error": "Missing cached data. Make sure initial, images, and seller steps are completed."},
            status=400
        )
        
    try:
        user = User.objects.get(username = username)
    except User.DoesNotExist:
        return Response({"User Does not exists. Sorry :( "})
        
    product = Product.objects.create(
        Product_Name=product_detail[0],
        Product_Category=product_detail[1],
        Product_Description=product_detail[2],
        Image_one=image_detail[0],
        Image_two=image_detail[1],
        Image_three=image_detail[2],
        Image_four=image_detail[3],
        Image_five=image_detail[4],
        Seller_Address=seller_detail[1],
        Price=seller_detail[2],
        Bought_Date=seller_detail[3],
        Seller_Name=user
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
