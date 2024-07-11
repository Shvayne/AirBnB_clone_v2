#!/usr/bin/python3
"""Fabric for automating deleting outdated files"""
from fabric.api import env, local, run, cd, lcd
import os

env.hosts = ['54.175.227.244', '54.197.129.188']

def do_clean(number=0):
    """Deletes outdated files"""
    num = 1 if int(num) == 0 else int(num)

    archives = sorted(os.listdir("versions"))
    for i in range(num):
        archvies.pop()
    with lcd("versions"):
        for a in archives:
            local("rm ./{}".format(a))
    with cd("/data/web_static/releases"):
        files = run("ls -tr").split()
        versions = [f for f in files if "web_static_" in f]
        for i in range(num):
            versions.pop()
        for version in versions:
            run("rm -rf ./{}".format(version))
