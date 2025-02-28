#!/usr/bin/python3
""" fab file """

from fabric.api import run, env, put
import os

env.hosts = ['44.200.180.194', '3.228.20.93']


def do_deploy(archive_path):
    """ deploy file """
    if not os.path.exists(archive_path):
        return False
    basename = os.path.basename(archive_path)
    path = '/data/web_static/releases'
    put(archive_path, '/tmp/')
    run('mkdir -p {}/{}'.format(path, basename.split('.')[0]))
    run('tar -zxf /tmp/{} -C /data/web_static/releases/{}'
        .format(basename, basename.split('.')[0]))
    run('rm /tmp/{}'.format(basename))
    run('mv {0}/{1}/web_static/* /data/web_static/releases/{1}'
        .format(path, basename.split('.')[0]))
    run('rm -rf {}/{}/web_static'.format(path, basename.split('.')[0]))
    run('rm -rf /data/web_static/current')
    run('ln -sf {}/{}/ /data/web_static/current'
        .format(path, basename.split('.')[0]))
    print('New version deployed!')
    return True
