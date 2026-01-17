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
        profile = UserprofileSeriaizer(data=request.data)
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
        user = user_profile.Username
        return Response(
            {
                "Response": {
                    "Message": "Got the user's detail",
                },
                "User's personal detail": {
                    "Firstname": user.first_name,
                    "Username": user.username,
                    "Email": user.email,
                },
                "Data": update_profile.data,
            },
            status=status.HTTP_200_OK,
        )


# User Profile Read View
class UserProfileSerializerReadView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk):
        user_profile = Userprofile.objects.get(pk=pk)
        read_data = UserprofileSeriaizer(user_profile)

        user = user_profile.Username
        return Response(
            {
                "Response": {
                    "Message": "Got the user's detail",
                },
                "User's personal detail": {
                    "Firstname": user.first_name,
                    "Username": user.username,
                    "Email": user.email,
                },
                "Data": read_data.data,
            }, status=status.HTTP_200_OK
        )


# User Profile Delete View
class UserProfileSerializerDeleteView(APIView):
    permission_classes = [AllowAny]
    def delete(self, request, pk):
        user_profile = Userprofile.objects.get(pk=pk)
        user_profile.delete()
        return Response({"Message":f"{user_profile} data deleted."})