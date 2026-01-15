from ..models.entities import Userprofile
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

def create_profile(profile):
    User_name = profile.validated_data['Username']
    Profilepic = profile.validated_data['Profile_Picture']
    Code = profile.validated_data['Country_Code']
    Number = profile.validated_data['Phone_Number']
    Location = profile.validated_data['Address']
    
    if not User.objects.filter(username = User_name).exists():
        raise ValidationError({"Message":f"User with the username {User_name} does not exists. Please signup an account first in order to continue. Thank you!"})
    
    Userprofile.objects.create(
        Username = User_name,
        Profile_Picture = profile.validated_data['Profile_Picture'],
        Country_Code = profile.validated_data['Profile_Picture'],
        Phone_Number = profile.validated_data['Profile_Picture'],
        Address = profile.validated_data['Profile_Picture'],
    )
    
    return Response({"Message":f"Profile for {User_name} successfully created!"})

