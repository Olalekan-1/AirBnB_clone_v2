#!/usr/bin/python3


"""Generates a .tgz archive from the contents of the web_static folder."""

from fabric.api import *
from datetime import datetime
import os


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
