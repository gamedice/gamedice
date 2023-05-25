from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from django.urls import path, include
from rest_framework import routers
from login.views import UserListView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls')),
    path('drf-auth/', include('rest_framework.urls')),
    path('api/v1/users/all', UserListView.as_view()),

]