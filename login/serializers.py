from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = Profile
        fields = '__all__'

class ExecutorSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    class Meta:
        model = User
        fields = '__all__'

