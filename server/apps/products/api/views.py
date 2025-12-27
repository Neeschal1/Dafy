from django.shortcuts import render
from .serializers import ProductSerializers
from rest_framework import generics
from apps.products.models.entities import Product
from rest_framework.permissions import AllowAny

class ProductSerializersView(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductSerializers