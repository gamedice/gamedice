from django.urls import path
from .views import *

urlpatterns = [
    path('', PostsAPIList.as_view()),
    path('<int:pk>/', PostsAPIDetail.as_view()),
    path('<post_id>/comments/', CommentsAPIList.as_view()),
]