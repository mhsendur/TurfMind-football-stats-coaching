from django.urls import path
from . import views

urlpatterns = [
    path('api/leagues/<str:league_name>/<str:season>/', views.LeagueTableView.as_view(), name='league-table'),
    path('api/clubs/<str:league_name>/<str:club_name>/<str:season>/', views.ClubDetailView.as_view(), name='club-detail'),
    ]
