from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import SignupSerializers, LoginSerializers
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from apps.accounts.services.login import login_user
from rest_framework.response import Response

class SignupSerializersView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = SignupSerializers

class LoginSerializersView(APIView):
    permission_classes=[AllowAny]
    def post(self, request):
        serializer = LoginSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        logged_in_user = login_user(serializer)
        if logged_in_user:
            return Response({'Message':f'Welcome, {logged_in_user.first_name}!'})
        