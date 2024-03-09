from fastapi import FastAPI
from tasks import add_task
from celery.result import AsyncResult
import time
app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/tasks/add")
async def add(x: int, y: int):
    return {"task_id", add_task.delay(x, y).id}
    

@app.get("/tasks/result")
async def task_result(task_id):
    res = AsyncResult(task_id)
    return {"status": res.ready()}