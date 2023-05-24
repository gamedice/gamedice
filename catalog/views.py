from django.shortcuts import render
from django_filters import FilterSet, NumberFilter, AllValuesFilter, ModelMultipleChoiceFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets
from rest_framework.pagination import PageNumberPagination
from .models import Genre, Company, Games
from .serializers import GenreSerializer, CompanySerializer, GamesSerializer, AnonsSerializer
from rest_framework import filters
from django.db.models import Max
from random import randint


class GamesFilter(FilterSet):
    min_rating = NumberFilter(field_name='rating', lookup_expr='gte')
    max_rating = NumberFilter(field_name='rating', lookup_expr='lte')
    genre_name = ModelMultipleChoiceFilter(field_name='genre__name', queryset=Genre.objects.all())
    company_name = ModelMultipleChoiceFilter(field_name='company__name', queryset=Company.objects.all())

    class Meta:
        model = Games
        fields = ('name', 'min_rating', 'max_rating', 'genre_name', 'company_name')


class GameAPIListPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 100


class GenreAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = Genre.objects.all().order_by('name')
    serializer_class = GenreSerializer
    pagination_class = GameAPIListPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']


class CompanyAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = Company.objects.all().order_by('name')
    serializer_class = CompanySerializer
    pagination_class = GameAPIListPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']


class GamesAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = Games.objects.all().order_by('name').filter(preview=True)
    serializer_class = GamesSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = GamesFilter
    # filterset_fields = ['genre', 'company']
    # search_fields = ['genre__name', 'name']
    pagination_class = GameAPIListPagination


class TopAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = Games.objects.all().filter(preview=True).order_by('-rating')
    serializer_class = GamesSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['rating']
    pagination_class = GameAPIListPagination


class AnonsAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = Games.objects.all().filter(preview=False).order_by('name')
    serializer_class = AnonsSerializer
    pagination_class = GameAPIListPagination


class RandomAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = Games.objects.all().filter(preview=True)
    serializer_class = GamesSerializer

    def get_queryset(self):
        max_id = Games.objects.all().aggregate(max_id=Max("id"))['max_id']
        while True:
            pk = randint(1, max_id)
            category = Games.objects.filter(pk=pk).filter(preview=True)
            if category:
                return category
