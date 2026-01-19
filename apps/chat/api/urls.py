from django.urls import path
from .views import *

urlpatterns = [
    path('askgoogle/', ConversationSerializersView.as_view(), name='ConversationSerializersView'),
    
    path('chatting/', chatview, name="chatview"),
    path('chatting/details/', chatviewdetails, name="chatviewdetails"),
]
