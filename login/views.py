from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from login.models import Profile
from login.serializers import UserSerializer


class UserListView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = UserSerializer
