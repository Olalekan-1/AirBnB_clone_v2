from fabric.api import run, local

def hello():
    print("Hello, Fabric!")

def deploy():
    local("git pull origin master")

