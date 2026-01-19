from django.urls import path
from .views import *

urlpatterns = [
    # Mandatory operations
    path('create/', ProductSerializersCreateView.as_view(),name='ProductSerializersCreateView'),
    path('update/<int:pk>/', ProductSerializersUpdateView.as_view(),name='ProductSerializersUpdateView'),
    path('read/<int:pk>/', ProductSerializersReadView.as_view(), name='ProductSerializersReadView'),
    path('delete/<int:pk>/', ProductSerializersDeleteView.as_view(), name='ProductSerializersDeleteView'),
    
    # Extras
    path('initial/', InitialProductDetailSerializersView.as_view(), name='InitialProductDetailSerializersView'),
    path('initial/images/', ProductImagesDetailSerializersView.as_view(), name='ProductImagesDetailSerializersView'),
    path('initial/images/seller/', ProductSellerDetailSerializersView.as_view(), name='ProductSellerDetailSerializersView'),
]