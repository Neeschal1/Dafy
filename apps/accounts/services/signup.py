from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

def signup(account):
    Full_Name = account.validated_data['first_name']
    Username = account.validated_data['username']
    Email = account.validated_data['email']
    Password = account.validated_data['password']
    
    if User.objects.filter(username = Username).exists():
        return Response({"Message":f"User already exists with the same username!"}, status=status.HTTP_400_BAD_REQUEST)
    
    if User.objects.filter(email = Email).exists():
        return Response({"Message":f"User with email: {Email} already exists. Please choose another email to create an account."}, status=status.HTTP_400_BAD_REQUEST)
    
    hashed_password = make_password(Password)
    
    user = User.objects.create(
        first_name = Full_Name,
        username = Username,
        email = Email,
        password = hashed_password,
        is_active = False
    )
    
    return Response({"Message":f"New account of {user.first_name} created!"}, status=status.HTTP_201_CREATED)