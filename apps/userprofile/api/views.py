from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import *
from ..services.profile import create_profile

# User's profile views
# User Profile serializer's view
class UserprofileSeriaizerCreateView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        profile = UserprofileSeriaizer(data = request.data)
        profile.is_valid(raise_exception=True)
        return create_profile(profile)
    
