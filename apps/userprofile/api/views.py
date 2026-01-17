from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import *
from rest_framework.response import Response
from django.contrib.auth.models import User
from ..services.profile import create_profile
from django.shortcuts import get_object_or_404
from rest_framework import status

# User Profile Create View
class UserprofileSeriaizerCreateView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        profile = UserprofileSeriaizer(data = request.data)
        profile.is_valid(raise_exception=True)
        return create_profile(profile)
    
# User Profile Update View
class UserProfileSerializerUpdateView(APIView):
    permission_classes = [AllowAny]
    def put(self, request, pk):
        user_profile = get_object_or_404(Userprofile, pk=pk)
        update_profile = UserprofileSeriaizer(user_profile, data=request.data)
        update_profile.is_valid(raise_exception=True)
        update_profile.save()
        return Response({"Message":"Profile successfully updated.", "Updated Data":update_profile.data}, status=status.HTTP_200_OK)