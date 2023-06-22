from django.test import TestCase
from blog.models import Posts, Comments
from django.contrib.auth.models import User


class PostsAndCommentsStrTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            username="username",
            email="username@gmail.com",
            password="username",
        )
        Posts.objects.create(
            title='Test post 1 title',
            contain='Contain of test post 1',
            is_published=True,
            user_id=User.objects.get(username='username').id,
        )
        Comments.objects.create(
            post_id=Posts.objects.get(title='Test post 1 title').id,
            user_id=User.objects.get(username='username').id,
            text='Comment for first post'
        )

    def test_str_to_return_post_title(self):
        post_1 = Posts.objects.get(title='Test post 1 title')
        self.assertEquals(str(post_1), post_1.title)

    def test_str_to_return_comments_text(self):
        comment_1 = Comments.objects.get(text='Comment for first post')
        self.assertEquals(str(comment_1), comment_1.text)



