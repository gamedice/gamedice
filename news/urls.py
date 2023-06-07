from django.urls import path
from news.views import NewsAPIList, NewsAPIDetailView

urlpatterns = [
    path('', NewsAPIList.as_view()),
    path('<int:pk>/', NewsAPIDetailView.as_view()),
]