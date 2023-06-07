from rest_framework import serializers
from catalog.models import Genre, Company, Games


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name', 'subscribe', )


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'biography', 'logo', )


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