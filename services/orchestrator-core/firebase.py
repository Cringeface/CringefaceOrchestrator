import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("C:/PyDEV/CringefaceOrchestrator/config/cringeface001-firebase-adminsdk-fbsvc-06e6a1fd42.json")
firebase_admin.initialize_app(cred, {"projectId": "cringeface001"})

db = firestore.client()

def save_message(message):
    doc_ref = db.collection("chat_messages").add({
        "content": message,
        "timestamp": firestore.SERVER_TIMESTAMP
    })
    return doc_ref.id