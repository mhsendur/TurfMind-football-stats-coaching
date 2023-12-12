from rest_framework import views, response, status  # Import status module here
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


class ClubDetailView(views.APIView):
    def get(self, request, league_name, club_name, season):
        document_id = f"{league_name}_{season}_{club_name}"

        try:
            db = firestore.client()
            
            # Get the reference to the specific document
            doc_ref = db.collection(u'clubs').document(document_id)
            doc = doc_ref.get()

            if doc.exists:
                # Convert the document to dictionary
                doc_data = doc.to_dict()

                # Calculate any additional metrics
                # calculate average xG:
                # doc_data['avg_xG'] = doc_data['total_xG'] / doc_data['matches_played']

                return response.Response(doc_data, status=status.HTTP_200_OK)
            else:
                return response.Response(
                    {"error": f"No data found for the specified club and season. Searched for document: {document_id}"},
                    status=status.HTTP_404_NOT_FOUND
                )
        except Exception as e:
            # Handle any other exceptions that occur
            return response.Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
