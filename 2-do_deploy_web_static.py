#!/usr/bin/python3
'''
This script distributes an archive to my web
servers, using the function do_deploy
'''

from fabric.api import put, run, env
import os

env.hosts = ['54.158.204.125', '54.236.47.6']


def do_deploy(archive_path):
    '''
    This function deploys the web_static directory
    to the server
    '''

    if not os.path.exists(archive_path):
        return False
    else:
        try:
            put(archive_path, '/tmp')
            filename = archive_path.split('/')[-1]
            archive_dir = filename.split('.')[0]
            run(f'mkdir -p /data/web_static/releases/{archive_dir}')
            run('tar -xzf /tmp/{} -C /data/web_static/releases/{}'.
                format(filename, archive_dir))

            run(f'rm -rf /tmp/{filename}')
            run(f'rm -rf /data/web_static/current')
            run('ln -s /data/web_static/current /data/web_static/releases/{}'.
                format(archive_dir))

            return True

        except Exception as e:
            return False
