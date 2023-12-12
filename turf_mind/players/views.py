
from rest_framework import views, response
from turf_mind.firebase import db

class PlayerStatsView(views.APIView):
    def get(self, request, league_name, season, team=None):
        # Query Firestore for the players data
        players_collection = db.collection(f'players_{league_name}')
        documents = players_collection.stream()

        # Process Firestore documents
        player_stats = []
        for doc in documents:
            doc_id = doc.id
            if season in doc_id:
                doc_data = doc.to_dict()
                for player in doc_data.get('data', []):
                    if not team or (team and player.get('team') == team):
                        player_stats.append(player)

        return response.Response(player_stats)