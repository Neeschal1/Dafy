from rest_framework.response import Response
from django.contrib.auth.models import User
from apps.userprofile.models.entities import Userprofile
from django.core.cache import cache

def seller_detail(seller):
    cache_key = seller.validated_data["Username"]
    try:
        user = User.objects.get(username=cache_key)
    except User.DoesNotExist:
        return Response({"Message": "User doesnot exists. Sorry :("})
    try:
        profile = Userprofile.objects.get(Username=user)
    except Userprofile.DoesNotExist:
        return Response({"Message": "User profile doesnot exists. Sorry :("})
    
    salesman_name = user.first_name
    salesman_address = profile.Address
    details = [
        salesman_name,
        salesman_address,
        seller.validated_data["Selling_Price"],
        seller.validated_data["Estimated_Bought_Date"],
    ]
    cache.set(f"seller_detail_{cache_key}", details, timeout=2000)
    return Response(
        {
            "Message": {
                "Details": {
                    "Initial Details": cache.get(cache_key),
                    "Images Details": cache.get(f"images_{cache_key}"),
                    "Sellers Detail": cache.get(f"seller_detail_{cache_key}"),
                }
            }
        }
    )
