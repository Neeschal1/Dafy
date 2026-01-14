from .serializers import *
from rest_framework.views import APIView
from rest_framework.permissions import *
from ..services.signup import signup
from rest_framework.response import Response
from rest_framework import status

# User account serializer's view
class UserSerializersView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        account = UserSerializers(data = request.data)
        account.is_valid(raise_exception=True)
        return signup(account)
        