from django.shortcuts import render
from .serializers import *
from rest_framework.views import APIView
from ..services.chats import chatting
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User

# View of serializer for short termed conversation with llm
class ConversationSerializersView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        query = ConversationSerializers(data=request.data)
        query.is_valid(raise_exception=True)
        
        # try:
        #     user = User.objects.get(pk=pk)
        # except User.DoesNotExist:
        #     return Response({"Message":"User doesnot exists. Please try again later!"})
        
        return chatting(query)