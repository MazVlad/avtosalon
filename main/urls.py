"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from .yasg import urlpatterns as doc_urls
from . import settings


urlpatterns = [
    path("admin/", admin.site.urls),
    path(r"api/car/", include("car.urls")),  # http://127.0.0.1:8000/api/car/
    path(
        r"api/customer/", include("customer.urls")
    ),  # http://127.0.0.1:8000/api/customer/
    path(
        r"api/provider/", include("provider.urls")
    ),  # http://127.0.0.1:8000/api/provider/
    path(
        "api/showroom/", include("showroom.urls")
    ),  # http://127.0.0.1:8000/api/showroom/
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
    path("api/v1/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/v1/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/v1/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]

urlpatterns += doc_urls


if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
