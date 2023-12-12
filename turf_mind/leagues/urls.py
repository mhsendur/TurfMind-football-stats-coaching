from django.urls import path
from . import views

urlpatterns = [
    path('league/', views.league_view, name='league'),
]
