from django.urls import path
from . import views

urlpatterns = [
    path('api/clubs/<str:league_name>/<str:club_name>/<str:season>/', views.ClubDetailView.as_view(), name='club-detail'),
    ]
