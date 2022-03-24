#!/usr/bin/python3
""" fab file """

from fabric.api import run, env
import os


env.hosts = ['44.192.23.250', '3.238.29.156', '3.236.241.248']

def test(archive_path):
    if not os.path.exists(archive_path):
        return False
    put('{}, /tmp/'.format(archive_path))
    run('tar zxf /tmp/{} -C /data/web_static/releases/{}/'
            .format(archive_path, archive_path.split('.')[0]))
    run('rm -r /tmp/{}'.format(archive_path))
    run('ln -sf /data/web_static/releases/{} /data/web_static/current/'/
            .format(archive_path.splite('.')[0]))
    return True
