from django.shortcuts import render
from .serializers import *
from rest_framework.views import APIView
from ..services.chats import chatting_stream
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from django.http import StreamingHttpResponse
from ..tasks import side_task
from django.core.cache import cache

# View of serializer for short termed conversation with llm
class ConversationSerializersView(APIView):
    parser_classes = [JSONParser]
    permission_classes = [AllowAny]
    def post(self, request):
        query = ConversationSerializers(data=request.data)
        query.is_valid(raise_exception=True)
        stream = chatting_stream(query)
        return StreamingHttpResponse(stream, content_type='text/plain')
  
# For testing purpose      
def chatview(request):
    side_task.delay()  # Trigger async Celery task
    return JsonResponse({"Message": "Celery task started!"})

def chatviewdetails(request):
    data = cache.get("celerydata")
    return JsonResponse({"Data": data})