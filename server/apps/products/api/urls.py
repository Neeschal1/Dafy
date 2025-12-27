from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductSerializersView.as_view(), name='ProductSerializersView')
]
