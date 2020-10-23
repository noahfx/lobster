import os
import time

TMP_DIR = "/tmp/lobster"

def get_tempdir():
    tmp_path = TMP_DIR
    if not os.path.isdir(tmp_path):
        os.mkdir(tmp_path)
    return tmp_path

def get_workingdir():
    tmp_dir = get_tempdir()
    dir_name = str(int(time.time()))
    path = os.path.join(tmp_dir, dir_name)
    os.mkdir(path)
    return path

def get_tmpfile(extension):
    file_name = '.'.join([str(int(time.time())), extension])
    return file_name

def get_album_dir(dir_name):
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)
    return dir_name
