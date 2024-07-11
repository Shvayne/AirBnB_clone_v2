#!/usr/bin/python3
"""this module contains functions to automate deployment using fabric"""
from datetime import datetime
from fabric.api import local, env, run, put
from os.path import isdir, isfile

env.hosts =['54.175.227.244', '54.197.129.188']
filename=""

def deploy():
    """Create and distribute archives to webservers"""
    archive = do_pack() if not filename else filename
    if not archive:
        print("Error creating archive.")
        return False
    return do_deploy(archive)

def do_pack():
    """create a .tgz from the webstatic folder"""
    try:
        now = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir('versions') is False:
            local("mkdir versions")
        filename = "versions/web_static_{}.tgz".format(now)
        print("Packing web_static to {}".format(filename))
        local("tar -cvzf {} web_static".format(filename))
        return filename
    except Exception:
        return None

def do_deploy(archive_path):
    """Distribute an archive to web servers"""
    if isfile(archive_path) is  False:
        return False
    remPath = archive_path.split('/')[-1]
    remExp = remPath.split('.')[0]

    if put(archive_path, "/tmp/").failed is True:
        print("Unable to upload archive to server\n")
        return False
    if (run("mkdir -p /data/web_static/releases/{}".format(remExp)).failed is True):
        print("Unable to create directory on server\n")
        return False
    if (run("tar -xzf /tmp/{} -C /data/web_static/releases/{}".format(remPath, remExp)).failed is True):
        print("unable to extract archive on server\n")
        return False
    if run("rm /tmp/{}".format(remPath)).failed is True:
        print("Unable to delete archive from server\n")
        return False
    if (run("mv /data/web_static/releases/{}/web_static/* " "/data/web_static/releases/{}".format(remExp, remExp)).failed is True):
        print("Unable to move archive contents to server directory\n")
        return False
    if (run("rm -rf /data/web_static/releases/{}/web_static".format(remExp)).failed is True):
        print("Unable to delete unnecessary empty folder\n")
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        print("Unable to delete existing symbolic link\n")
        return False
    if (run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(remExp)).failed is True):
        print("Unable to create symbolic link to new release\n")
        return False
    print("New version deployed successfully!\n")
    return True

