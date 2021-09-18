"""
参考文档：
https://docs.celeryproject.org/en/stable/
https://flower.readthedocs.io/en/latest/
https://github.com/mher/flower
启动任务：celery -A learn.learn_celery worker --loglevel=INFO
"""

from celery import Celery, app

app = Celery(
    "hello",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0",
)

import time


@app.task
def hello():
    time.sleep(3)
    return "Hello, world!"
