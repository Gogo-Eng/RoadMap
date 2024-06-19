#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of
the web_static folder of your AirBnB Clone repo, using the function do_pack
"""
from fabric.api import *
from datetime import datetime
import os

datetime_format = "%Y%m%d%H%M%S"


def do_pack():
    """
    the function that helps  generate a .tgz archive from the contents of the
    web_static folder of your AirBnB Clone repo,
    """
    local('sudo mkdir -p versions')
    current_time = datetime.now()

    name_format = current_time.strftime(datetime_format)

    local(f'sudo tar -cvzf versions/web_static_{name_format}.tgz web_static')

    file_path = f'versions/web_static_{name_format}.tgz'
    file_size = os.path.getsize(file_path)
    print(f'web_static packed: {file_path} -> {file_size}Bytes')
    return file_path
