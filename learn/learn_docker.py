"""
参考文档：
https://docker-py.readthedocs.io/en/stable/
https://github.com/docker/docker-py
https://pypi.org/project/docker/
"""
import docker

client = docker.from_env()
print(client.images.list())