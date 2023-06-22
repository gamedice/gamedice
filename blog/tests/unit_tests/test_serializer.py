from django.test import TestCase
from django.contrib.auth.models import User

from blog.models import Posts, Comments
from blog.serializers import PostsSerializer, CommentsSerializer


class PostsAndCommentsSerializerTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            username="username",
            email="username@gmail.com",
            password="username",
        )
        Posts.objects.create(
            title='Test post 1 title',
            photo=None,
            contain='Contain of test post 1',
            is_published=True,
            user_id=User.objects.get(username='username').id,
        )
        Posts.objects.create(
            title='Test post 2 title',
            photo=None,
            contain='Contain of test post 2',
            is_published=True,
            user_id=User.objects.get(username='username').id,
        )
        Comments.objects.create(
            post_id=Posts.objects.get(title='Test post 1 title').id,
            user_id=User.objects.get(username='username').id,
            text='First comment for first post from username',
        )
        Comments.objects.create(
            post_id=Posts.objects.get(title='Test post 1 title').id,
            user_id=User.objects.get(username='username').id,
            text='Second comment for first post from username',
        )

    def test_post_serializer(self):
        user_1 = User.objects.get()
        post_1 = Posts.objects.get(title='Test post 1 title')
        post_2 = Posts.objects.get(title='Test post 2 title')

        data = PostsSerializer([post_1, post_2], many=True).data

        post_1_date = PostsSerializer(post_1).data.get('time_created')
        post_2_date = PostsSerializer(post_2).data.get('time_created')

        expected_data = [
            {
                'id': post_1.id,
                'title': 'Test post 1 title',
                'photo': None,
                'contain': 'Contain of test post 1',
                'time_created': post_1_date,
                'is_published': True,
                'user': user_1.id,
                'username': 'username',
            },
            {
                'id': post_2.id,
                'title': 'Test post 2 title',
                'photo': None,
                'contain': 'Contain of test post 2',
                'time_created': post_2_date,
                'is_published': True,
                'user': user_1.id,
                'username': 'username',
            },
        ]

        self.assertEquals(expected_data, data)

    def test_comments_serializer(self):
        user_1 = User.objects.get()
        post_1 = Posts.objects.get(title='Test post 1 title')

        comment_1 = Comments.objects.get(text='First comment for first post from username')
        comment_2 = Comments.objects.get(text='Second comment for first post from username')

        data = CommentsSerializer([comment_1, comment_2], many=True).data

        comment_1_date = CommentsSerializer(comment_1).data.get('date')
        comment_2_date = CommentsSerializer(comment_2).data.get('date')

        expected_data = [
            {
                'post': post_1.id,
                'user': user_1.id,
                'username': 'username',
                'text': 'First comment for first post from username',
                'date': comment_1_date,
            },
            {
                'post': post_1.id,
                'user': user_1.id,
                'username': 'username',
                'text': 'Second comment for first post from username',
                'date': comment_2_date,
            },
        ]

        self.assertEquals(expected_data, data)
