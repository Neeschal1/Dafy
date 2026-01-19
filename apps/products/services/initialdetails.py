from ..api.serializers import InitialProductDetailSerializers
from rest_framework.response import Response
from django.core.cache import cache

def initial_details(detail):
    cache_key = detail.validated_data['Username']
    name = detail.validated_data['Product_Name']
    category = detail.validated_data['Product_Category']
    description = detail.validated_data['Product_Description']
    
    details = [name, category, description]
    cache.set(cache_key, details, timeout=2000)

    return Response({"Message":cache.get(cache_key)})