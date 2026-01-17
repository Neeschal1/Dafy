from django.urls import path
from .views import *

urlpatterns = [
    path('', UserSerializersCreateView.as_view(), name='UserSerializersCreateView'),
    path('profile/update/<int:pk>/', UserSeriaizerUpdateView.as_view(), name='UserSeriaizerUpdateView'),
]