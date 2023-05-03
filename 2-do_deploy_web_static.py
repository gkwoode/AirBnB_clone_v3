#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py) that 
distributes an archive to your web servers, using the function do_deploy
"""

import os.path
from fabric.api import *
from datetime import datetime

env.hosts = ['18.206.208.237', '54.157.153.196']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """Distributes an archive to your web servers"""
    if not os.path.isfile(archive_path):
        return False

    try:
        archive_file = archive_path.split("/")[-1]
        archive_name = archive_file.split(".")[0]
        archive_folder = "/data/web_static/releases/" + archive_name

        put(archive_path, "/tmp/{}".format(archive_file))

        run("mkdir -p {}".format(archive_folder))
        run("tar -xzf /tmp/{} -C {}".format(archive_file, archive_folder))
        run("rm -rf /tmp/{}".format(archive_file))
        run("mv {}/web_static/* {}/".format(archive_folder, archive_folder))
        run("rm -rf {}/web_static".format(archive_folder))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(archive_folder))

        print("New version deployed!")
        return True

    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
