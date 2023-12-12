from django.shortcuts import render, get_object_or_404
from .models import Club

def calculate_league_table(clubs):

    sorted_clubs = sorted(clubs, key=lambda x: (-x.points, x.goals_scored))

    position = 1
    league_table = []
    for club in sorted_clubs:
        club.position = position
        league_table.append(club)
        position += 1

    return league_table

def league_view(request, season=None):
    # Fetch clubs from the database
    clubs = Club.objects.all()

    if season:
        # Filter clubs by the selected season
        clubs = clubs.filter(season=season)

    league_table = calculate_league_table(clubs)

    available_seasons = Club.objects.values_list('season', flat=True).distinct()

    return render(request, 'leagues/league_template.html', {
        'league_table': league_table,
        'available_seasons': available_seasons,
        'selected_season': season,
    })
