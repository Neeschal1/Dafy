from django.urls import path
from .views import *

urlpatterns = [
    path('askgoogle/', ConversationSerializersView.as_view(), name='ConversationSerializersView')
]
