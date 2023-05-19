from django.urls import path
from .views import *

urlpatterns = [
    path('', NewsAPIList.as_view()),
    path('<int:pk>/', NewsAPIDetailView.as_view()),
]