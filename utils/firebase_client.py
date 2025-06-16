import firebase_admin
from firebase_admin import credentials, firestore 
import os

cred_path = os.path.join(os.path.dirname(__file__), "../gymsoftware-b4745-firebase-adminsdk-fbsvc-93f6a914ba.json")
cred = credentials.Certificate(os.path.abspath(cred_path))
firebase_admin.initialize_app(cred)  

db_firestore = firestore.client()

def get_firestore_client():
    return db_firestore