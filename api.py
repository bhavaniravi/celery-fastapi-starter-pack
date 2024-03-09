from fastapi import FastAPI
from tasks import add as add_task
from celery.result import AsyncResult

app = FastAPI()


@app.get("/")
def hello_world():
    return {"Hello": "World"}


@app.get("/tasks/add")
def add(x: int, y: int):
    return {"task_id": add_task.delay(x, y).id}


@app.get("/tasks/result")
def task_status(task_id: str):
    res = AsyncResult(task_id).ready()
    return {"task_id": task_id, "result": res}