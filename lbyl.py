"""Two Philosophy
1. Look before you leap
2. It's easier to ask forgiveness than permission"""


import os

p = ''

if os.path.exists(p):
    process_file(p)
else:
    print('No such file as {}'.format(p))

    # Different Way

x = ''

try:
    process_file(x):
except OSError as e:
    print("Could not process file because{}".format(str(e)))



def make_at(path,dir_name):
    original_path = os.getcwd()
    os.chdir(path)
    os.mkdir(dir_name)
    os.chdir(original_path)


def make_at1(path,dir_name):
    original_path = os.getcwd()
    try:
        os.chdir(path)
        os.mkdir(dir_name)
    finally:
        os.chdir(original_path)