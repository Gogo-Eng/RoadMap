#!/usr/bin/python3
"""
Fabfile to distribute an archive to a web server.
"""
from fabric.api import *
from datetime import datetime
import os

env.user = 'ubuntu'
env.hosts = ['100.26.233.141', '100.25.2.227']
env.key_filename = '~/.ssh/school'


def do_pack():
    """
    the function that helps generate a .tgz archive from the contents of the
    web_static folder of your AirBnB Clone repo, using the function do_pack
    """
    local('sudo mkdir -p versions')
    current_time = datetime.now()

    name_format = current_time.strftime(datetime_format)

    create = local(f'sudo tar -cvzf versions/web_static_{name_format}.tgz\
                   web_static')

    file_path = f'versions/web_static_{name_format}.tgz'
    file_size = os.path.getsize(file_path)
    print(f'web_static packed: {file_path} -> {file_size}Bytes')

    if create.succeeded:
        return file_path
    else:
        return None


def do_deploy(archive_path):
    """
    Fabric script (based on the file 1-pack_web_static.py) that distributes
    an archive to your web servers, using the function do_deploy
    """
    if not os.path.exists(archive_path):
        print(f"Archive {archive_path} does not exist.")
        return False

    archive_name = os.path.basename(archive_path)
    release_dir = '/data/web_static/releases'
    archive_dir = f'{release_dir}/{archive_name.split(".")[0]}'

    try:
        put(archive_path, '/tmp/')
        run(f'mkdir -p {archive_dir}')
        run(f'tar -xzf /tmp/{archive_name} -C {archive_dir}')
        run(f'rm /tmp/{archive_name}')
        run(f'mv {archive_dir}/web_static/* {archive_dir}/')
        run(f'rm -rf {archive_dir}/web_static')
        run('rm -rf /data/web_static/current')
        run(f'ln -s {archive_dir} /data/web_static/current')
        print("New version deployed!")
        return True
    except Exception as error:
        print(f'Deployment failed: {error}')
        return False
