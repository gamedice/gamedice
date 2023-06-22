from django.test import TestCase
from catalog.models import Genre, Games, Company


class StrTestCase(TestCase):
    def setUp(self):
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
    def test_str_genre(self):
        genre_1 = Genre.objects.get()
        self.assertEquals(str(genre_1), genre_1.name)

    def test_str_company(self):
        company_1 = Company.objects.get()
        self.assertEquals(str(company_1 ), company_1 .name)

    def test_str_game(self):
        game_1 = Games.objects.get()
        self.assertEquals(str(game_1), game_1.name)