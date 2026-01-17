from django.urls import path
from .views import *

urlpatterns = [
    path('', UserprofileSeriaizerCreateView.as_view(), name='UserprofileSeriaizerCreateView')
]
