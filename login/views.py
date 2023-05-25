from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .models import *
from .serializers import *


class UserListView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = UserSerializer
