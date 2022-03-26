#!/usr/bin/python3
""" python file for fabric """


from fabric.api import local
import os
import datetime


def do_pack():
    """ pack web files """

    if not os.path.isdir("versions"):
        os.mkdir("versions")
    filename = 'versions/web_static_' + datetime.datetime.now()\
        .strftime("%G%m%d%H%M%S") + '.tgz'
    print('Packing web_static to {}'.format(filename))
    local('tar -zcvf {} web_static'.format(filename))
    print('web_static packed: {} -> {}Bytes'\
            .format(filename, os.path.getsize(filename)))
