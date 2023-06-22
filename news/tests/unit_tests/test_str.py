from django.test import TestCase
from news.models import News
from django.contrib.auth.models import User


class NewsStrTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            username="username",
            email="username@gmail.com",
            password="username",
        )
        News.objects.create(
            title='Test news 1 title',
            contain='Contain of news 1',
            user_id=User.objects.get(username='username').id,
        )

    def test_str_to_return_news_title(self):
        news_1 = News.objects.get(title='Test news 1 title',)
        self.assertEquals(str(news_1), news_1.title)
