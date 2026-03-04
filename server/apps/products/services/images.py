from rest_framework.response import Response
from django.core.cache import cache
from django.contrib.auth.models import User

def product_images(image):
    cache_key = image.validated_data['Username']
    imageone = image.validated_data['Image_one']
    imagetwo = image.validated_data['Image_two']
    imagethree = image.validated_data['Image_three']
    imagefour = image.validated_data['Image_four']
    imagefive = image.validated_data['Image_five']
    
    try:
        user = User.objects.get(username = cache_key)
    except User.DoesNotExist:
        return Response({"Message":f"User with the username: {cache_key} does not exists. Please signup and account first and then try again!"})
    
    if user:
        details = [imageone, imagetwo, imagethree, imagefour, imagefive]
        cache.set(f"images_{cache_key}", details, timeout=2000)
        
        return Response({"Response":{"Details":{
            "Initial Details":cache.get(cache_key),
            "Images Details": cache.get(f"images_{cache_key}")
        }}})
    else:
        return Response({"Message":"Something error occred. Might be you don't have a stable network connection."})