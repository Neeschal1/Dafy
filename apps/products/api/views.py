from django.shortcuts import render
from .serializers import *
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from ..services.products import create_a_new_product
from rest_framework.response import Response
from ai.semantic_search import selected_product
from rest_framework import status


# Product Serializers View for creating a new product
class ProductSerializersCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        prod = ProductSerializers(data=request.data)
        prod.is_valid(raise_exception=True)
        return create_a_new_product(prod)


# Product Serializers View for updating a new product
class ProductSerializersUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        prod = get_object_or_404(Product, pk=pk)
        update_prod = ProductSerializers(prod, data=request.data)
        update_prod.is_valid(raise_exception=True)
        update_prod.save()
        user = prod.Seller_Name
        return Response(
            {
                "Response": {
                    "Message": "Product detail updated successfully.",
                },
                "User's personal detail": {
                    "Firstname": user.first_name,
                    "Username": user.username,
                    "Email": user.email,
                },
                "Data": update_prod.data,
            },
            status=status.HTTP_200_OK,
        )


# Product Serializers View for reading an existing product
class ProductSerializersReadView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk):
        same_products = []
        prod = Product.objects.get(pk=pk)
        user_product = ProductSerializers(prod)
        user = prod.Seller_Name
        similar_products = selected_product(user_product.data["Product_Description"])

        for same in similar_products:
            try:
                same_prod = Product.objects.filter(Product_Description=same).first()
                if same_prod:
                    same_products.append(ProductSerializers(same_prod).data)
            except Exception as e:
                return Response(str(e))

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
                "Data": user_product.data,
                "Other Similar Products": same_products,
            },
            status=status.HTTP_200_OK,
        )


# Product Serializers View for deleting an existing product
class ProductSerializersDeleteView(APIView):
    permission_classes = [AllowAny]

    def delete(self, request, pk):
        prod = Product.objects.get(pk=pk)
        prod.delete()
        return Response({"Message": "Product deleted successfully."})
