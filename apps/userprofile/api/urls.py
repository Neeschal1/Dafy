from django.urls import path
from .views import *

urlpatterns = [
    path('create/', UserprofileSeriaizerCreateView.as_view(), name='UserprofileSeriaizerCreateView'),
    path('update/<int:pk>/', UserProfileSerializerUpdateView.as_view(), name='UserProfileSerializerUpdateView'),
    path('read/<int:pk>/', UserProfileSerializerReadView.as_view(), name='UserProfileSerializerReadView'),
    path('delete/<int:pk>/', UserProfileSerializerDeleteView.as_view(), name='UserProfileSerializerDeleteView'),
]