from django.urls import path
from .views import *

urlpatterns = [
    path('create/', ProductSerializersCreateView.as_view(), name='ProductSerializersCreateView'),
    path('update/<int:id>/', ProductSerializersUpdateView.as_view(), name='ProductSerializersUpdateView'),
]