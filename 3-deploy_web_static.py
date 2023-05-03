#!/usr/bin/python3
"""
Fabric script (based on the file 2-do_deploy_web_static.py) that creates and 
distributes an archive to your web servers, using the function deploy:
"""

from datetime import datetime
from fabric.api import local, env, run, put
import os

env.hosts = ['18.206.208.237', '54.157.153.196']

def do_pack():
    """Creates a compressed archive of web_static folder"""

    try:
        if not os.path.exists('versions'):
            os.mkdir('versions')
        now = datetime.now().strftime('%Y%m%d%H%M%S')
        filename = f"versions/web_static_{now}.tgz"
        local("tar -cvzf {} web_static".format(filename))
        return filename
    except Exception:
        return None

def do_deploy(archive_path):
    """Distributes archive to web servers"""

    if not os.path.exists(archive_path):
        return False

    try:
        put(archive_path, "/tmp/")

        filename = os.path.basename(archive_path)
        directory_name = filename.split('.')[0]

        run("mkdir -p /data/web_static/releases/{}/".format(directory_name))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(filename, directory_name))
        run("rm /tmp/{}".format(filename))
        run("mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/".format(directory_name, directory_name))
        run("rm -rf /data/web_static/releases/{}/web_static".format(directory_name))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(directory_name))

        return True

    except Exception:
        return False

def deploy():
    """Calls do_pack and do_deploy functions to deploy web_static"""

    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
