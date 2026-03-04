from rest_framework import serializers
from ..models.entities import Userprofile

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