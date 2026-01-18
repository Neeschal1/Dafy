from django.contrib import admin
from django.urls import path, include, re_path
from .views import defaultscreen
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)
from rest_framework.permissions import IsAdminUser, AllowAny
from drf_yasg.views import get_schema_view  # type: ignore
from drf_yasg import openapi  # type: ignore
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

schema_view = get_schema_view(
    openapi.Info(
        title="Dafy Backend API Docs",
        default_version="v1",
        description="API documentation for Dafy, an e-commerce mobile application.",
    ),
    public=True,
    permission_classes=(IsAdminUser,),
    authentication_classes=(SessionAuthentication, BasicAuthentication),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    
    # For swagger documentations
    re_path(r"^docs/$", schema_view.with_ui("swagger", cache_timeout=0), name="swagger-ui"),
    re_path(r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="redoc"),
    
    # For jwt tokens
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # For whole applications
    path("", defaultscreen, name="defaultscreen"),
    path("accounts/", include("apps.accounts.api.urls")),
    path("profile/", include("apps.userprofile.api.urls")),
    path("payments/", include("apps.payments.api.urls")),
    path("products/", include("apps.products.api.urls")),
    path("chat/", include("apps.chat.api.urls")),
]
