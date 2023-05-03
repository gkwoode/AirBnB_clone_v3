#!/usr/bin/python3
"""
 Fabric script that generates a .tgz archive from the contents of the web_static 
 folder of your AirBnB Clone repo, using the function do_pack.
"""

from datetime import datetime
from fabric.api import local, env

def do_pack():
    """Generate .tgz archive"""
    try:
        now = datetime.now().strftime('%Y%m%d%H%M%S')
        local("mkdir -p versions")
        path = "versions/web_static_{}.tgz".format(now)
        local("tar -cvzf {} web_static".format(path))
        return path
    except:
        return None
