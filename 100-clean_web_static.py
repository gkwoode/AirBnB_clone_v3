#!/usr/bin/python3
"""
Write a Fabric script (based on the file 3-deploy_web_static.py) 
that deletes out-of-date archives, using the function do_clean:
"""

from fabric.api import *
from datetime import datetime
import os

env.hosts = ['18.206.208.237', '54.157.153.196']
env.user = 'ubuntu'

def do_clean(number=0):
    """Deletes out-of-date archives."""

    try:
        number = int(number)
    except:
        return False

    if number < 0:
        return False
    elif number == 0 or number == 1:
        number = 1
    else:
        number += 1

    archives = sorted(os.listdir('versions'))
    if len(archives) >= number:
        archives_to_delete = archives[:-number]
        for archive in archives_to_delete:
            path = os.path.join('versions', archive)
            local('rm -f {}'.format(path))

    archives = run('ls /data/web_static/releases')
    archives = archives.split('\n')
    if len(archives) >= number:
        archives_to_delete = archives[:-number]
        for archive in archives_to_delete:
            if archive != 'test':
                path = os.path.join('/data/web_static/releases', archive)
                run('sudo rm -rf {}'.format(path))

    return True
