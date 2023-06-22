from django.urls import reverse
from rest_framework.test import APITestCase
from catalog.models import Company, Genre, Games
from conf.settings import SERVER_PORT


class ApiTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        company_1 = Company.objects.create(
            name='b_test',
            biography='test 1'
        )
        company_2 = Company.objects.create(
            name='a_test',
            biography='test 1'
        )
        genre_1 = Genre.objects.create(
            name='b_test',
            subscribe='Contain of test post 1',
        )
        genre_2 = Genre.objects.create(
            name='a_test',
            subscribe='Contain of test post 2',
        )
        game_1 = Games.objects.create(
            name='b_test',
            subscribe='test game 1',
            date_created='2023-06-08',
            company_id=company_1.id,
            genre_id=genre_1.id,
            rating=0.0,
            count_player=0.0,
            preview=True,
        )
        game_2 = Games.objects.create(
            name='test game 2',
            subscribe='test game 2',
            date_created='2023-06-08',
            company_id=company_1.id,
            genre_id=genre_1.id,
            rating=0.0,
            count_player=0.0,
            preview=False,
        )
        game_3 = Games.objects.create(
            name='a_test',
            subscribe='test game 1',
            date_created='2023-06-08',
            company_id=company_1.id,
            genre_id=genre_1.id,
            rating=0.0,
            count_player=0.0,
            preview=True,
        )

    def test_getting_company(self):
        company_1 = Company.objects.get(pk=1)
        company_2 = Company.objects.get(pk=2)
        url = reverse('company-list')
        response = self.client.get(url)
        data = response.data
        expected_data = [
            {
                'id': company_2.id,
                'name': 'a_test',
                'biography': 'test 1',
                'logo': None,
            },
            {
                'id': company_1.id,
                'name': 'b_test',
                'biography': 'test 1',
                'logo': None,
            },
        ]
        self.assertEqual(expected_data, data)


    def test_getting_genre(self):
        genre_1 = Genre.objects.get(pk=1)
        genre_2 = Genre.objects.get(pk=2)
        url = reverse('genre-list')
        response = self.client.get(url)
        data = response.data
        expected_data = [
            {
                'id': genre_2.id,
                'name': 'a_test',
                'subscribe': 'Contain of test post 2'
            },
            {
                'id': genre_1.id,
                'name': 'b_test',
                'subscribe': 'Contain of test post 1'
            }
        ]
        self.assertEqual(expected_data, data)


    def test_getting_game(self):
        game_1 = Games.objects.get(pk=1)
        game_2 = Games.objects.get(pk=2)
        game_3 = Games.objects.get(pk=3)
        url = f'http://127.0.0.1:{SERVER_PORT}/catalog/game/'
        response = self.client.get(url)
        data = response.data
        expected_data = [
            {
                'id': game_3.id,
                'name': 'a_test',
                'photo': None,
                'subscribe': 'test game 1',
                'genre': 'b_test',
                'company': 'b_test',
                'date_created': '2023-06-08',
                'rating': 0.0,
                'count_player': 0.0,
            },
            {
                'id': game_1.id,
                'name': 'b_test',
                'photo': None,
                'subscribe': 'test game 1',
                'genre': 'b_test',
                'company': 'b_test',
                'date_created': '2023-06-08',
                'rating': 0.0,
                'count_player': 0.0,

            }
        ]
        self.assertEqual(expected_data, data)


    def test_getting_anons(self):
        game_1 = Games.objects.get(pk=1)
        game_2 = Games.objects.get(pk=2)
        game_3 = Games.objects.get(pk=3)
        url = f'http://127.0.0.1:{SERVER_PORT}/catalog/anons/'
        response = self.client.get(url)
        data = response.data
        expected_data = [
            {
                'id': game_2.id,
                'name': 'test game 2',
                'photo': None,
                'subscribe': 'test game 2',
                'genre': 'b_test',
                'company': 'b_test',
                'date_created': '2023-06-08',
            }
        ]
        self.assertEqual(expected_data, data)
