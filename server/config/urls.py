from django.contrib import admin
from django.urls import path, include
from .views import defaultscreen

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', defaultscreen, name='defaultscreen'),
    path('accounts/', include('apps.accounts.api.urls'))
]
