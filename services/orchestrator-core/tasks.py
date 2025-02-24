from celery import Celery
import firebase_admin
from firebase_admin import firestore

app = Celery("orchestrator_core", broker="redis://localhost:6379/0")

# Initialize Firebase (ensure this is only initialized once, consider moving to main.py or a singleton)
cred = credentials.Certificate("C:/PyDEV/CringefaceOrchestrator/config/cringeface001-firebase-adminsdk-fbsvc-06e6a1fd42.json")
firebase_admin.initialize_app(cred, {"projectId": "cringeface001"})
db = firestore.client()


@app.task
def process_task(task_data):
    message = task_data["message"]
    firebase_id = task_data["firebase_id"]

    # Simulate NLP processing
    processed_message = f"Processed: {message} (NLP output)"

    # Update Firebase with result
    db.collection("chat_messages").document(firebase_id).update({
        "processed_content": processed_message,
        "status": "completed"
    })

    return {"status": "completed", "data": processed_message}