from django.test import TestCase
from django.contrib.auth.models import User

from blog.models import Posts, Comments
from blog.serializers import CommentsSerializer
from conf.settings import URL_BACK


class GetCommentsToPostTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            username="username",
            email="username@gmail.com",
            password="username",
        )
        User.objects.create_user(
            username="username_2",
            email="username_2@gmail.com",
            password="username_2",
        )
        Posts.objects.create(
            title='Test post 1 title',
            photo=None,
            contain='Contain of test post 1',
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
            user_id=User.objects.get(username='username_2').id,
            text='Second comment for first post from username_2',
        )

    def test_get_two_comments_to_first_post(self):
        user_1 = User.objects.get(username='username')
        user_2 = User.objects.get(username='username_2')
        post_1 = Posts.objects.get(title='Test post 1 title')

        comment_1 = Comments.objects.get(text='First comment for first post from username')
        comment_2 = Comments.objects.get(text='Second comment for first post from username_2')

        comment_1_date = CommentsSerializer(comment_1).data.get('date')
        comment_2_date = CommentsSerializer(comment_2).data.get('date')

        expected_data = [
            {
                'post': post_1.id,
                'user': user_2.id,
                'username': 'username_2',
                'text': 'Second comment for first post from username_2',
                'date': comment_2_date,
            },
            {
                'post': post_1.id,
                'user': user_1.id,
                'username': 'username',
                'text': 'First comment for first post from username',
                'date': comment_1_date,
            },
        ]

        url = f'{URL_BACK}/blog/1/comments/'
        response = self.client.get(url)

        received_data = response.data

        self.assertEquals(received_data, expected_data)
