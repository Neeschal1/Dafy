from django.urls import path
from .views import *

urlpatterns = [
    # User accounts CRUD operations
    path('create/', UserSerializersCreateView.as_view(), name='UserSerializersCreateView'),
    path('update/<int:pk>/', UserSeriaizerUpdateView.as_view(), name='UserSeriaizerUpdateView'),
    path('read/<int:pk>/', UserSerializerReadView.as_view(), name='UserSerializerReadView'),
    path('delete/<int:pk>/', UserSerializerDeleteView.as_view(), name='UserSerializerDeleteView'),
    
    # Account Login
    path('login/', UserLoginSerializersView.as_view(), name='UserLoginSerializersView'),
]