from django.urls import path
from blog.views import PostsAPIList, PostsAPIDetail, CommentsAPIList, UsersPostsAPIList, UsersPostsAPIDetail

urlpatterns = [
    path('', PostsAPIList.as_view()),
    path('<int:pk>/', PostsAPIDetail.as_view()),
    path('<post_id>/comments/', CommentsAPIList.as_view()),
    path('users_post/<user_id>', UsersPostsAPIList.as_view()),
    path('users_post/<user_id>/<int:pk>', UsersPostsAPIDetail.as_view()),
]
