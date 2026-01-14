from django.urls import path
from .views import UserSerializersView

urlpatterns = [
    path('', UserSerializersView.as_view(), name='UserSerializersView')
]