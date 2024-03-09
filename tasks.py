from celery import Celery
from dotenv import load_dotenv
import os
import time


load_dotenv()

app = Celery('tasks', broker=os.getenv('CELERY_BROKER_URL'), backend=os.getenv('CELERY_RESULT_BACKEND'))

@app.task
def add_task(x, y):
    time.sleep(30)
    return x + y