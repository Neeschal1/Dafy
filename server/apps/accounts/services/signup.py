from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError


def create_user(validated_data):
    Username = validated_data["username"]
    Password = validated_data["password"]
    First_Name = validated_data["first_name"]
    Last_Name = validated_data["last_name"]
    Email = validated_data["email"]

    hashed_password = make_password(Password)

    if User.objects.filter(email=Email).exists():
        raise ValidationError({"email": ["User with this email already exists!"]})

    user = User.objects.create(
        username=Username,
        first_name=First_Name,
        last_name=Last_Name,
        email=Email,
        password=hashed_password,
    )

    return user
