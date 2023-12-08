from fabric.api import run, local

if "__name__" == __main__:
    def hello():
        print("Hello, Fabric!")

def deploy():
    local("git pull origin master")

