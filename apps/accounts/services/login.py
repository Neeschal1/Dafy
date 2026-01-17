from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import check_password

def login_account(serializer):
    email = serializer.validated_data['Email']
    password = serializer.validated_data['Password']
    
    try:
        user = User.objects.get(email = email)
    except User.DoesNotExist:
        return Response({"Message":f"User with the email: {email} didn't exists. Please create an account first and then try logging in the account."}, status=status.HTTP_400_BAD_REQUEST)
    
    if not check_password(password, user.password):
        return Response({"Message":"Invalid Credentials! Please check your password and then try again!"})
    
    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)
    refresh_token = str(refresh)
    
    return Response({"Response":{
        "Message":"Account successfully logged in",
        "Username":f"Welcome! {user.username}",
        "Tokens" : {
            "access token" : access_token,
            "refresh token" : refresh_token,
        }
    }})