#!/usr/bin/python3
"""module to generate a .tgz archive"""
from fabric import task
from datetime import datetime
import os

@task
def do_pack(c):
    """
    Generate a .tgz archive from the contents of the websatic folder
    """
    versions_dir = 'versions'
    if not os.path.exists(versions_dir):
        os.makedirs(versions_dir)

    now = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_path = f"{versions_dir}/web_static_{now}.tgz"
    result = c.local('tar -cvzf {} web_static'.format(archive_path))

    if results.failed:
        return None
    else:
        return archive_path
