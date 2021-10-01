import docker
import os

client = docker.from_env()
print(client.containers.list())

cont = client.containers.get('785a3e84f8')
print(cont.attrs['Config']['Image'])