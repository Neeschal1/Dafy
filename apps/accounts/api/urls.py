from django.urls import path
from .views import *

urlpatterns = [
    path('', UserSerializersCreateView.as_view(), name='UserSerializersCreateView'),
    path('profile/update/<int:pk>/', UserprofileSeriaizerUpdateView.as_view(), name='UserprofileSeriaizerUpdateView'),
    path('profile/', UserprofileSeriaizerView.as_view(), name='UserprofileSeriaizerView'),
]