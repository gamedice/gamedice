from django.urls import path, include
from rest_framework import routers
from catalog.views import GamesAPIView, GenreAPIView, CompanyAPIView, TopAPIView, AnonsAPIView

router = routers.SimpleRouter()
router.register(r'game', GamesAPIView),
router.register(r'genre', GenreAPIView),
router.register(r'company', CompanyAPIView),
router.register(r'rating', TopAPIView),
router.register(r'anons', AnonsAPIView),
# router.register(r'random', RandomAPIView),


urlpatterns = [
    path('', include(router.urls)),
]
