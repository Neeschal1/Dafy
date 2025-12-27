from django.urls import path
from . import views

urlpatterns = [
    path('', views.SignupSerializersView.as_view(), name='SignupSerializersView'),
    path('login/', views.LoginSerializersView.as_view(), name='LoginSerializersView')
]
