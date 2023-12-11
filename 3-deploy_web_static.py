#!/usr/bin/python3


"""Generates a .tgz archive from the contents of the web_static folder."""

from fabric.api import *
from datetime import datetime
import os
from os.path import exists

env.hosts = ['54.237.66.181', '54.82.199.141']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder."""
    # Create the versions directory if it doesn't exist
    local("mkdir -p versions")

    # Generate the archive filename using the current date and time
    now = datetime.utcnow()
    archive_name = "web_static_{}{}{}{}{}{}.tgz".format(
        now.year, now.month, now.day, now.hour, now.minute, now.second
    )

    # Create the archive
    result = local("tar -czvf versions/{} web_static".format(archive_name))

    if result.succeeded:
        return "versions/{}".format(archive_name)
    else:
        return None


def deploy(archive_path):
    """Deploys the archive file to the web server"""
    archive_path = do_pack()
    if not archive_path:
        return False

    try:
        print("Deploying {}".format(archive_path))
        put(archive_path, '/tmp/')

        file_name = archive_path.split("/")[-1].split(".")[0]

        sudo('mkdir -p /data/web_static/releases/{}/'.format(file_name))

        with cd('/data/web_static/releases/{}'.format(file_name)):
            # sudo('mkdir -p /data/web_static/releases/{}/'.format(file_name))
            sudo('tar -xzf /tmp/{}.tgz'.format(file_name))
            sudo('mv /data/web_static/releases/{}/web_static/* .'.format(
                file_name))
            sudo('rm -rf /data/web_static/releases/{}/web_static'.format(
                file_name))

        sudo('rm -rf /data/web_static/current')
        path = '/data/web_static/current'
        sudo('ln -s /data/web_static/releases/{}/ {}'.format(file_name, path))

        return True

    except Exception as e:
        print("Deployment failed: {}".format(str(e)))
        return False
