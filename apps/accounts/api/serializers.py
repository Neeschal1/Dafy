from rest_framework import serializers
from django.contrib.auth.models import User
from ..models.entities import Userprofile

# User account serializers
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
        
# User's Profile serializer
class UserprofileSeriaizer(serializers.ModelSerializer):
    class Meta:
        model = Userprofile
        fields = ['Username', 'Profile_Picture', 'Country_Code', 'Phone_Number', 'Address']
        extra_kwargs = {
            'Username' : {'required' : True},
            'Country_Code' : {'required' : True},
            'Phone_Number' : {'required' : True},
            'Address' : {'required' : True},
        }