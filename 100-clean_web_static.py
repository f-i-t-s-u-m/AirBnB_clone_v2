#!/usr/bin/python3
""" fab file """

from fabric.api import run, local, env, put
import os
import datetime

env.hosts = ['44.200.180.194', '3.228.20.93']

filename = 'versions/web_static_' + datetime.datetime.now()\
        .strftime("%G%m%d%H%M%S") + '.tgz'


def do_pack():
    """ pack web files """

    if not os.path.isdir("versions"):
        os.mkdir("versions")
    print('Packing web_static to {}'.format(filename))
    local('tar -zcvf {} web_static'.format(filename))
    print('web_static packed: {} -> {}Bytes'.format(
        filename, os.path.getsize(filename)))
    return filename


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


def deploy():
    """ deploy all """
    do_pack()
    result = do_deploy(filename)
    return result


def do_clean(number=0):
    """deletes out-of-date archives"""
    number = int(number)
    archives = sorted(os.listdir('versions'), reverse=True)
    # print(type(number))
    if number <= 1:
        number = 1
    for tgz in archives[number:]:
        tgz_path = 'versions/' + tgz
        local("rm versions/{}".format(tgz))
    for tgz in archives[number:]:
        tgz_path = 'versions/' + tgz
        run("rm -rf /data/web_static/releases/{}"
            .format(tgz.replace(".tgz", "")))
