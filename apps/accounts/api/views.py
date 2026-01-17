from .serializers import *
from rest_framework.views import APIView
from rest_framework.permissions import *
from django.contrib.auth.models import User
from rest_framework.response import Response
from ..services.signup import signup
from ..services.profile import create_profile

# User's account views
# User account create serializer's view
class UserSerializersCreateView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        account = UserSerializers(data = request.data)
        account.is_valid(raise_exception=True)
        return signup(account)
    
# User Profile serializer's update view
class UserprofileSeriaizerUpdateView(APIView):
    permission_classes = [IsAuthenticated, AllowAny]
    def put(self, request, pk):
        user = User.objects.filter(pk = pk).exists()
        update_profile = UserprofileSeriaizer(user, data=request.data)
        update_profile.is_valid(raise_exception=True)
        return Response({"Message":f"User's detail updated successfully!", "New data":update_profile.data})




# User's profile views      
# User Profile serializer's view
class UserprofileSeriaizerView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        profile = UserprofileSeriaizer(data = request.data)
        profile.is_valid(raise_exception=True)
        return create_profile(profile)
    
