from django.urls import path
from .views import *

urlpatterns = [
    path('create/', ProductSerializersView.as_view(), name='ProductSerializersView')
]
