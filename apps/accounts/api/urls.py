from django.urls import path
from .views import *

urlpatterns = [
    path('create/', UserSerializersCreateView.as_view(), name='UserSerializersCreateView'),
    path('update/<int:pk>/', UserSeriaizerUpdateView.as_view(), name='UserSeriaizerUpdateView'),
    path('read/<int:pk>/', UserSerializerReadView.as_view(), name='UserSerializerReadView'),
    
]