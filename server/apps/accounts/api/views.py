from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import SignupSerializers
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

class SignupSerializersView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = SignupSerializers