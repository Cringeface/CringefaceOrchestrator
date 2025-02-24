from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import firebase_admin
from firebase_admin import credentials, firestore
from tasks import process_task  # Import Celery task from tasks.py

app = FastAPI(title="Cringeface Orchestrator Core")

# Initialize Firebase
cred = credentials.Certificate("C:/PyDEV/CringefaceOrchestrator/config/cringeface001-firebase-adminsdk-fbsvc-06e6a1fd42.json")
firebase_admin.initialize_app(cred, {"projectId": "cringeface001"})
db = firestore.client()


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            message = {"sender": "Sayle", "content": data}

            # Save to Firebase
            msg_id = save_message_to_firebase(message)

            # Process via Celery
            result = process_task.delay({"message": data, "firebase_id": msg_id})

            # Send response back (simplified)
            await websocket.send_text(f"Processing: {data} (Task ID: {result.id})")
    except WebSocketDisconnect:
        await websocket.close()


def save_message_to_firebase(message):
    doc_ref = db.collection("chat_messages").add({
        "content": message["content"],
        "sender": message["sender"],
        "timestamp": firestore.SERVER_TIMESTAMP
    })
    return doc_ref.id


@app.get("/")
async def root():
    return {"message": "Cringeface Orchestrator Core is running!"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001)