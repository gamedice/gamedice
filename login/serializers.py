from rest_framework import serializers
from login.models import Profile, Favorites
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = Profile
        fields = ('user', 'photo', 'like', )

class ExecutorSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    class Meta:
        model = User
        fields = '__all__'

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorites
        fields = ('id', 'user', 'game', )