
from django.urls import path
from . import views
from .views import player_page

urlpatterns = [
    path('api/players/<str:league_name>/<str:season>/', views.PlayerStatsView.as_view(), name='player-stats-season'),
    path('api/players/<str:league_name>/<str:team>/<str:season>/', views.PlayerStatsView.as_view(), name='player-stats-season-team'),
    path('<str:league_name>/<str:season>/', player_page, name='player-page'),
    path('<str:league_name>/<str:team>/<str:season>/', player_page, name='player-team-page'),
]
