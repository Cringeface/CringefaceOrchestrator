from celery import Celery

app = Celery("orchestrator_core", broker="redis://localhost:6379/0")

@app.task
def process_task(task_data):
    print(f"Processing task: {task_data}")
    return {"status": "completed", "data": task_data}