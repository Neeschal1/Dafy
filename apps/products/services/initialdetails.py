from ..api.serializers import InitialProductDetailSerializers
from rest_framework.response import Response
from django.core.cache import cache
from ..tasks import description_embeddings
from ai.embeddings import initialize_embeddings
from django.contrib.auth.models import User

def initial_details(detail):
    cache_key = detail.validated_data['Username']
    name = detail.validated_data['Product_Name']
    category = detail.validated_data['Product_Category']
    description = detail.validated_data['Product_Description']
    
    try:
        user = User.objects.get(username = cache_key)
    except User.DoesNotExist:
        return Response({"Message":f"User with the username: {cache_key} does not exists. Please signup and account first and then try again!"})
    
    if user:
        initialize_embeddings.delay(cache_key, name, category, description)
        details = [cache_key, name, category, description]
        cache.set(cache_key, details, timeout=2000)
        return Response({"Message":cache.get(cache_key)})
    else:
        return Response({"Message":"Something error occred. Might be you don't have a stable network connection."})