"""Gamedice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
<<<<<<< HEAD
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
=======
from django.urls import path, include

>>>>>>> main

from login.views import UserListView

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('api/v1/users/all', UserListView.as_view()),
=======
    path('catalog/', include('catalog.urls')),
]
>>>>>>> main

    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
