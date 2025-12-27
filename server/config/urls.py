from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('accounts/', include('apps.accounts.api.urls')),
    path('products/', include('apps.products.api.urls')),
]  
