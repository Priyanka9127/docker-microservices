from celery import Celery
import os
import datetime

CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://redis:6379/0')
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', 'redis://redis:6379/0')

celery = Celery('tasks', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)

@celery.task
def add(x, y):
    task_id = celery.current_task.id
    current_time = datetime.datetime.now()
    print(f"Worker task ID: {task_id}, Time: {current_time}, Result: {x + y}")
    return x + y