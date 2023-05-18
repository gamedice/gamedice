from rest_framework import serializers
from .models import Posts, Comments

class PostsSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = Posts
        fields = '__all__'

class CommentsSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    post = serializers.StringRelatedField()
    class Meta:
        model = Comments
        fields = '__all__'