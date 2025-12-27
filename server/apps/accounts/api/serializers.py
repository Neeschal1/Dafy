from rest_framework import serializers
from django.contrib.auth.models import User
from apps.accounts.services.signup import create_user

class SignupSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'is_active']
        extra_kwargs = {
            'username' : {'required' : True},
            'last_name' : {'required' : True},
            'first_name' : {'required' : True},
            'email' : {'required' : True},
            'password' : {'required' : True, 'write_only' : True},
            'is_active' : {'read_only' :True}
        }
    
    def create(self, validated_data):
        new_user = create_user(validated_data)
        return new_user