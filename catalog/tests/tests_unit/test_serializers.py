from django.test import TestCase
from catalog.models import Company, Genre, Games
from catalog.serializers import CompanySerializer, GenreSerializer, GamesSerializer, AnonsSerializer


class SerializerTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        company = Company.objects.create(
            name='Test company 1',
            biography='test 1'
        )

        genre = Genre.objects.create(
            name='Test genre 1',
            subscribe='Contain of test post 1',
        )
        game = Games.objects.create(
            name='b_test',
            subscribe='test game 1',
            date_created='2023-06-08',
            company_id=company.id,
            genre_id=genre.id,
            rating=0.0,
            count_player=0.0,
            preview=True,
        )

    def test_company_get(self):
        company_1 = Company.objects.get()
        data = CompanySerializer(company_1).data
        expected_data = {
                'id': company_1.id,
                'name': 'Test company 1',
                'biography': 'test 1',
                'logo': None
            }
        self.assertEqual(expected_data, data)

    def test_genre_get(self):
        genre_1 = Genre.objects.get()
        data = GenreSerializer(genre_1).data
        expected_data = {
                'id': genre_1.id,
                'name': 'Test genre 1',
                'subscribe': 'Contain of test post 1'
            }
        self.assertEquals(expected_data, data)

    def test_game_get(self):
        game_1 = Games.objects.get()
        data = GamesSerializer(game_1).data
        expected_data = {
                'id': game_1.id,
                'name': 'b_test',
                'photo': None,
                'subscribe': 'test game 1',
                'genre': 'Test genre 1',
                'company': 'Test company 1',
                'date_created': '2023-06-08',
                'rating': 0.0,
                'count_player': 0.0,
            }
        self.assertEquals(expected_data, data)

    def test_anons_get(self):
        game_1 = Games.objects.get()
        data = AnonsSerializer(game_1).data
        expected_data = {
                'id': game_1.id,
                'name': 'b_test',
                'photo': None,
                'subscribe': 'test game 1',
                'genre': 'Test genre 1',
                'company': 'Test company 1',
                'date_created': '2023-06-08',
            }
        self.assertEquals(expected_data, data)
