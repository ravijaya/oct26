from zipfile import ZipFile
from glob import glob


def make_archive(archive_name, *args):
    """variable len argument"""

    with ZipFile(archive_name, mode='w') as zf:
        """context manager"""
        for file_name in args:
            zf.write(file_name)
            print(f'{file_name}: added')


if __name__ == '__main__':
    make_archive('src.zip', *glob('*.py'))
