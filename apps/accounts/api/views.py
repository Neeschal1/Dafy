from .serializers import *
from rest_framework.views import APIView
from rest_framework.permissions import *
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from ..services.signup import signup

# User account create serializer's view
class UserSerializersCreateView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        account = UserSerializers(data = request.data)
        account.is_valid(raise_exception=True)
        return signup(account)
    
# User account serializer's update view
class UserSeriaizerUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    def put(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        update_profile = UserSerializers(user, data=request.data)
        update_profile.is_valid(raise_exception=True)
        update_profile.save()
        return Response({"Message":"User's detail updated successfully!", "New data":update_profile.data})

# User account serializer's read view
class UserSerializerReadView(APIView):
    permission_classes=[AllowAny]
    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        read_user = UserSerializers(user)
        return Response({"Message":"User's data fetched successfully.", "Data: ":read_user.data})

# User account serializer's delete view
class UserSerializerDeleteView(APIView):
    permission_classes = [AllowAny]
    def delete(self, request, pk):
        user = User.objects.get(pk=pk)
        user.delete()
        return Response({"Message":"User's account successfully deleted."})