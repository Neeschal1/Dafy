from rest_framework import serializers
from django.contrib.auth.models import User

# User account create serializers
class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password', 'is_active']
        extra_kwargs = {
            'first_name': {'required': True},
            'username': {'required': True},
            'email': {'required': True},
            'password': {'required': True, 'write_only': True},
            'is_active': {'read_only': True},
        }

# User account login serializers   
class UserLoginSerializers(serializers.Serializer):
    Email = serializers.EmailField()
    Password = serializers.CharField()
