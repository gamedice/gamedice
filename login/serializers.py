from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = Profile
        fields = '__all__'


class ExecutorSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class FavoriteItemSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username', read_only=True)
    game_name = serializers.CharField(source='game.name', read_only=True)
    photo = serializers.ImageField(source='game.photo')
    subscribe = serializers.CharField(source='game.subscribe')

    class Meta:
        model = Favorites
        fields = ['user_id', 'user_name', 'game_id' ,'game_name', 'photo', 'subscribe']

class FavoriteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorites
        fields = ['game']
