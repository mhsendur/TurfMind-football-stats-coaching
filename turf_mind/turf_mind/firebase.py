
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('/Users/mhsendur/Desktop/va325-data/turfmind-59773-firebase-adminsdk-6escg-395c3b93a2.json')

firebase_admin.initialize_app(cred)

db = firestore.client()
