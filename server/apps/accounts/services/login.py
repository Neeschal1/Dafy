from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from django.contrib.auth.hashers import check_password

def login_user(serializer):
    Email = serializer.validated_data['Email']
    Password = serializer.validated_data['Password']
    
    try:
        user = User.objects.get(email = Email)
    except User.DoesNotExist:
        raise ValidationError({'Message':'User not found. Please Signup a new account first!'})
    
    match_password = check_password(Password, user.password)
    
    if not match_password:
        raise ValidationError({'Message' : 'Invalid Credentials!'})
    
    return user