from django.urls import path
from .views import *

urlpatterns = [
    path('pay/', PaymentSerializersView.as_view(), name="PaymentSerializersView")
]
