import os, sys

sys.path.append(os.getcwd())

from learn.learn_celery import hello
result = hello.delay()
print(result.get(timeout=4))