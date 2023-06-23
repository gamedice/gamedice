from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from django.urls import path, include
from .views import *

urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls')),
    path('drf-auth/', include('rest_framework.urls')),
    path('api/v1/users/all', UserAPIList.as_view()),
    path('api/v1/users/<int:pk>', UserAPIUpdate.as_view()),
    path('api/v1/userdelete/<int:pk>', UserAPIDestroy.as_view()),
    path('api/v1/favorites/<int:user_id>', UserFavoritesView.as_view(), name='user_favorites'),
    # path('favorites/', FavoriteList.as_view(), name='favorites-list'),
    path('api/v1/favorites/add/', FavoriteCreate.as_view(), name='favorites-create'),
]