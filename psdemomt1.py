import threading
from time import sleep
from random import random


def worker(delay):
    """function for the child"""
    t_name = threading.current_thread().name
    t_id = threading.current_thread().ident
    sleep(delay)
    print(t_name, 'waited for the  :', delay)


def main():
    """parent/main thread"""

    for item in range(1, 6):
        value = random()
        t = threading.Thread(target=worker, args=(value,), name=f't{item}')
        t.start()

    print('main thread prepares to terminates')


if __name__ == '__main__':
    main()