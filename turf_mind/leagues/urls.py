from django.urls import path
from . import views

urlpatterns = [
    path('api/leagues/<str:league_name>/<str:season>/', views.LeagueTableView.as_view(), name='league-table'),
    path('<str:league_name>/<str:season>/', views.league_page, name='league-page'),
    ]
