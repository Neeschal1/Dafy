from django.shortcuts import render
from .serializers import *
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from ..services.products import create_a_new_product
from rest_framework.response import Response
from rest_framework import status

# Product Serializers View for creating a new product
class ProductSerializersCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        prod = ProductSerializers(data = request.data)
        prod.is_valid(raise_exception=True)
        return create_a_new_product(prod)

# Product Serializers View for updating a new product
class ProductSerializersUpdateView(APIView):
    permission_classes = [AllowAny]
    def put(self, request, pk):
        prod = get_object_or_404(Product, pk=pk)
        update_prod = ProductSerializers(prod, data=request.data)
        update_prod.is_valid(raise_exception=True)
        user = prod.Seller_Name
        return Response(
            {
                "Response": {
                    "Message": "Got the user's detail",
                },
                "User's personal detail": {
                    "Firstname": user.first_name,
                    "Username": user.username,
                    "Email": user.email,
                },
                "Data": update_prod.data,
            }, status=status.HTTP_200_OK
        )
        