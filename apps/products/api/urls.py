from django.urls import path
from .views import *

urlpatterns = [
    path('newproduct/', ProductSerializersView.as_view(), name='ProductSerializersView')
]
