from django.urls import path
from .views import *

urlpatterns = [
    path('', UserSerializersView.as_view(), name='UserSerializersView'),
    path('profile/', UserprofileSeriaizerView.as_view(), name='UserprofileSeriaizerView')
]