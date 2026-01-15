from .serializers import *
from rest_framework.views import APIView
from rest_framework.permissions import *
from ..services.signup import signup
from ..services.profile import create_profile

# User account serializer's view
class UserSerializersView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        account = UserSerializers(data = request.data)
        account.is_valid(raise_exception=True)
        return signup(account)
        
# User Profile serializer's view
class UserprofileSeriaizerView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        profile = UserprofileSeriaizer(data = request.data)
        profile.is_valid(raise_exception=True)
        return create_profile(profile)