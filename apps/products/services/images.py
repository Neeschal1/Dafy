from rest_framework.response import Response
from django.core.cache import cache

def product_images(image):
    cache_key = image.validated_data['Username']
    imageone = image.validated_data['Image_one']
    imagetwo = image.validated_data['Image_two']
    imagethree = image.validated_data['Image_three']
    imagefour = image.validated_data['Image_four']
    imagefive = image.validated_data['Image_five']
    
    details = [imageone, imagetwo, imagethree, imagefour, imagefive]
    cache.set(f"images_{cache_key}", details, timeout=600)
    
    return Response({"Response":{"Details":{
        "Initial Details":cache.get(cache_key),
        "Images Details": cache.get(f"images_{cache_key}")
    }}})