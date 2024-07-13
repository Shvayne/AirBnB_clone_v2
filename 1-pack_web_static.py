#!/usr/bin/python3
"""module to generate a .tgz archive"""
from fabric import task
from datetime import datetime
from os.path import isdir

def do_pack(c):
    """Generate a .tgz archive from the contents of the websatic folder"""
    try:
        now = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir('versions') is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(now)
        local("tar -cvzf {} web_static/*".format(file_name))
        return file_name
    except Exception:
        return None

