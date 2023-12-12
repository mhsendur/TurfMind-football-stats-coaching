
from django.urls import path
from . import views

urlpatterns = [
    path('api/players/<str:league_name>/<str:season>/', views.PlayerStatsView.as_view(), name='player-stats-season'),
    
    path('api/players/<str:league_name>/<str:team>/<str:season>/', views.PlayerStatsView.as_view(), name='player-stats-season-team'),
]
