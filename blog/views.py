from django.shortcuts import render
from blog.serializers import PostsSerializer, CommentsSerializer
from rest_framework import generics
from blog.models import Posts, Comments


class PostsAPIList(generics.ListCreateAPIView):
    queryset = Posts.objects.filter(is_published=True).order_by("-time_created")
    serializer_class = PostsSerializer


class PostsAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer


class CommentsAPIList(generics.ListCreateAPIView):
    # queryset = Comments.objects.filter(post=post__id)
    # queryset = Comments.objects.all()
    serializer_class = CommentsSerializer

    def get_queryset(self, *args, **kwargs):
        return Comments.objects.filter(post=self.kwargs['post_id']).order_by("-date")




