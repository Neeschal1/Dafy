from django.shortcuts import render
from .serializers import *
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from ..services.products import create_a_new_product

# Product Serializers View for creating a new product
class ProductSerializersView(APIView):
    permission_classes = [IsAuthenticated, AllowAny]
    def post(self, request):
        prod = ProductSerializers(data = request.data)
        prod.is_valid(raise_exception=True)
        return create_a_new_product(prod)
        