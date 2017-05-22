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
    path = "/".join([tmp_dir, dir_name])
    os.mkdir(path)
    return path
