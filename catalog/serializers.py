from rest_framework import serializers
from .models import Genre, Company, Games


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class GamesSerializer(serializers.ModelSerializer):
    genre = serializers.StringRelatedField()
    company = serializers.StringRelatedField()
    class Meta:
        model = Games
        fields = ('id', 'name', 'photo', 'subscribe', 'genre', 'company', 'date_created', 'rating', 'count_player', )


class AnonsSerializer(serializers.ModelSerializer):
    genre = serializers.StringRelatedField()
    company = serializers.StringRelatedField()

    class Meta:
        model = Games
        fields = ('id', 'name', 'photo', 'subscribe', 'genre', 'company', 'date_created')