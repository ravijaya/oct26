"""directory listing"""

import os


def ls(dir_path='.'):
    try:
        for item in os.listdir(dir_path):
            print(item)
    except FileNotFoundError as err:
        print(err)


ls(r'c:\users\')
