import os
import pandas as pd
import firebase_admin
from firebase_admin import credentials, firestore

# Initialise Firebase
cred = credentials.Certificate("/path/to/firestore")
firebase_admin.initialize_app(cred)
db = firestore.client()


def upload_csv_to_firestore(csv_path, collection_name, document_name):
    df = pd.read_csv(csv_path)

    # Convert DataFrame to a dictionary
    data = df.to_dict(orient='records')

    try:
        # Create a document with the specified document name and store the data
        db.collection(collection_name).document(document_name).set({"title": document_name, "data": data})
        print(f"Successfully uploaded '{document_name}' to Firestore collection '{collection_name}'")
    except Exception as e:
        print(f"Error uploading '{document_name}': {e}")

def process_folder(folder_path, collection_prefix):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.csv'):
                csv_path = os.path.join(root, file)

                # Create a document name based on file's relative path
                rel_path = os.path.relpath(csv_path, start=folder_path)
                document_name = os.path.splitext(rel_path)[0].replace(os.sep, '_')
                collection_name = f"{collection_prefix}_{os.path.basename(root)}"
                print(f"Uploading file: {file}")
                upload_csv_to_firestore(csv_path, collection_name, document_name)

# Upload club data
process_folder('cleaned_club_data', 'clubs')

# Upload player data
process_folder('cleaned_player_data', 'players')
