from django.shortcuts import render
from .serializers import *
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from ..services.products import create_a_new_product
from ..services.initialdetails import initial_details
from ..services.images import product_images
from ..services.seller import seller_detail
from ..services.similar_prods import other_similar_products
from ..models.entities import Product
from rest_framework.response import Response
from ai.vector.operations.fetch import fetch_products_vector
from rest_framework import generics
from .pagination import *
from rest_framework import status


# All Product serializer for viewing the products
class FetchAllProducts(generics.ListAPIView):
    serializer_class = ProductSerializers
    queryset = Product.objects.all()
    permission_classes = [AllowAny]

# Product Serializers View for creating a new product
class ProductSerializersCreateView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('Username') or request.data.get('username')
        if not username:
            return Response({"Message":"Expecting 'Username'."})
        return create_a_new_product(username)


# Product Serializers View for initial product Details
class InitialProductDetailSerializersView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        detail = InitialProductDetailSerializers(data=request.data)
        detail.is_valid(raise_exception=True)
        return initial_details(detail)

# Product Images Serializer view for providing image details
class ProductImagesDetailSerializersView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        image = ProductImagesDetailSerializers(data=request.data)
        image.is_valid(raise_exception=True)
        return product_images(image)

# Product's Seller Serializer view for seller's detail
class ProductSellerDetailSerializersView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        seller = ProductSellerDetailSerializers(data=request.data)
        seller.is_valid(raise_exception=True)
        return seller_detail(seller)
    
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


# # Product Serializers View for reading an existing product
class ProductSerializersReadView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, pk):
        prod = Product.objects.get(pk=pk)
        user_product = ProductSerializers(prod)
        user = prod.Seller_Name
        selected_product = user_product.data["Product_ID"]
        other_products = []
        
        all_products = Product.objects.all()
        for prods in all_products:
            other_products.append(prods.Product_ID)
        
        similar_products = fetch_products_vector(selected_product, other_products)
        return other_similar_products(similar_products, selected_product, prod, user)


# Product Serializers View for deleting an existing product
class ProductSerializersDeleteView(APIView):
    permission_classes = [AllowAny]

    def delete(self, request, pk):
        prod = Product.objects.get(pk=pk)
        prod.delete()
        return Response({"Message": "Product deleted successfully."})
