from django.shortcuts import render
from rest_framework import generics
from news.serializers import NewsSerializer
from news.models import News


class NewsAPIList(generics.ListAPIView):
    queryset = News.objects.all().order_by("-time_created")
    serializer_class = NewsSerializer


class NewsAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

