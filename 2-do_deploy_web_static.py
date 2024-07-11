#!/usr/bin/python3
"""this module contains the do_deploy function"""
import os.path
from fabric.api import env, put, run

env.hosts = ['54.197.129.188', '54.175.227.244']

def do_deploy(archive_path):
    """Distribute an archive to web servers"""
    if os.path.isfile(archive_path) is False:
        return False
    remPath = archive_path.split('/')[-1]
    remExt = remPath.split('.')[0]

    if put(archive_path, "/tmp/").failed is True:
        print("Unable to upload archive to server\n")
        return False
    if (run("mkdir -p /data/web_static/releases/{}".format(RemExt)).failed is True):
        print("Unable to create directory on server\n")
        return False
    if (run("tar -xzf /tmp/{} -C /data/web_static/release/{}".format(remPath, remExt)).failed is True):
        print("Unable to extract archive on server\n")
        return False
    if run("rm /tmp/{}".format(remPath)).failed is True:
        print("unable to delete archive from server\n")
        return False
    if (run("mv /data/web_static/releases/{}/web_static/* " "/data/web_static/releases/{}".format(remPath, remExt)).failed is True):
        print("Unable to move archive contents to serve directory\n")
        return False
    if (run("rm -rf /data/web_static/releases/{}/web_static".format(RemExt)).failed is True):
        print("Unable to delete unnecessary empty folder\n")
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        print("Unable to delete existing symbolic link\n")
        return False
    if (run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(RemExt)).failed is True):
        print("Unable to create symbolic link to new release\n")
        return False
    print("New version deployed successfully!\n")
    return True
