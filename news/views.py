from django.shortcuts import render
from rest_framework import generics
from .serializers import NewsSerializer
from .models import News

class NewsAPIList(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class NewsAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

