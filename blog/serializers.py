from rest_framework import serializers
from blog.models import Posts, Comments


class PostsSerializer(serializers.ModelSerializer):
    username = serializers.StringRelatedField(source='user')

    class Meta:
        model = Posts
        fields = ('id', 'title', 'photo', 'contain', 'time_created', 'is_published', 'user', 'username', )


class CommentsSerializer(serializers.ModelSerializer):
    username = serializers.StringRelatedField(source='user')

    class Meta:
        model = Comments

        # fields = ('post', 'text', 'date', 'user_name', )
        fields = ('post', 'user', 'username', 'text', 'date', )
        # read_only_fields = ('post', 'text', 'date', 'user_name', )
        # extra_kwargs = {'user': {'write_only': True}}

    # def get_user(self, obj):
    #     return str(obj.user.username)
