from django.test import TestCase
from django.contrib.auth.models import User

from news.models import News
from news.serializers import NewsSerializer


class NewsSerializerTestCase(TestCase):

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
        News.objects.create(
            title='Test news 2 title',
            contain='Contain of news 2',
            user_id=User.objects.get(username='username').id,
        )

    def test_news_serializer(self):
        news_1 = News.objects.get(title='Test news 1 title')
        news_2 = News.objects.get(title='Test news 2 title')

        data = NewsSerializer([news_1, news_2], many=True).data

        news_1_date = NewsSerializer(news_1).data.get('time_created')
        news_2_date = NewsSerializer(news_2).data.get('time_created')

        expected_data = [
            {
                'id': news_1.id,
                'title': 'Test news 1 title',
                'photo': None,
                'contain': 'Contain of news 1',
                'time_created': news_1_date,
            },
            {
                'id': news_2.id,
                'title': 'Test news 2 title',
                'photo': None,
                'contain': 'Contain of news 2',
                'time_created': news_2_date,
            },
        ]

        self.assertEquals(expected_data, data)
