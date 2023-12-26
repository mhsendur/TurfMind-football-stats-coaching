from django.shortcuts import render
from rest_framework import views, response, status  
from turf_mind.firebase import db
from google.cloud.firestore_v1.base_query import FieldFilter
from firebase_admin import firestore

class LeagueTableView(views.APIView):
    def get(self, request, league_name, season):
        try:
            db = firestore.client()
            
            # Get all documents from the 'clubs' collection
            clubs_query = db.collection(u'clubs').stream()

            # Filter documents by league and season
            league_table = []
            for doc in clubs_query:
                doc_data = doc.to_dict()
                doc_id = doc.id 
                if doc_id.startswith(f"{league_name}_{season}_"):
                    league_table.append(doc_data)

            # If league_table is empty, send a not found response
            if not league_table:
                return response.Response(
                    {"error": f"No data found for league: {league_name}, season: {season}"},
                    status=status.HTTP_404_NOT_FOUND
                )

            # Otherwise, return the league table data
            return response.Response(league_table, status=status.HTTP_200_OK)

        except Exception as e:
            # Handle any other exceptions that occur
            return response.Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

def league_page(request, league_name, season):
    context = {
        'league_name': league_name,
        'season': season,
    }
    return render(request, 'leagues/index.html', context)
