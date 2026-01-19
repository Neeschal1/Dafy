from ..api.serializers import InitialProductDetailSerializers
from rest_framework.response import Response

def initial_details(detail):
    name = detail.validated_data['Product_Name']
    category = detail.validated_data['Product_Category']
    description = detail.validated_data['Product_Description']
    
    return Response({"Message":{"Product Details":{"Product Name":name, "Product Category":category, "Product Description":description}}})