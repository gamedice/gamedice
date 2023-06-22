from django_filters import FilterSet, NumberFilter, AllValuesFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from catalog.models import Genre, Company, Games
from catalog.serializers import GenreSerializer, CompanySerializer, GamesSerializer, AnonsSerializer
from rest_framework import filters



class GamesFilter(FilterSet):
    min_rating = NumberFilter(field_name='rating', lookup_expr='gte')
    max_rating = NumberFilter(field_name='rating', lookup_expr='lte')
    genre_name = AllValuesFilter(field_name='genre__name')
    company_name = AllValuesFilter(field_name='company__name')

    class Meta:
        model = Games
        fields = ('name', 'min_rating', 'max_rating', 'genre_name', 'company_name')


class GenreAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = Genre.objects.all().order_by('name')
    serializer_class = GenreSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']


class CompanyAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = Company.objects.all().order_by('name')
    serializer_class = CompanySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']


class GamesAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = Games.objects.all().order_by('name').filter(preview=True)
    serializer_class = GamesSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = GamesFilter


class TopAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = Games.objects.all().filter(preview=True).order_by('-rating')
    serializer_class = GamesSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['rating']


class AnonsAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = Games.objects.all().filter(preview=False).order_by('name')
    serializer_class = AnonsSerializer



