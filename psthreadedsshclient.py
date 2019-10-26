"""threaded ssh client"""
import logging
import threading
import pyexcel
from pssshclient import ssh_client

logging.basicConfig(format='%(asctime)s:%(threadName)s:%(message)s', filename='access22.log')
target_file = 'sshresponse.log'

"""https://pastebin.com/raw/iHAPV0iD"""


def ssh_handler(host, port, user, pwd, job):
    """child thread"""
    t_name = threading.current_thread().name
    payload = ssh_client(host, port, user, pwd, job)
    logging.info('done successfully')

    caption = f'{t_name} ran {job} @ {host}'

    with open(target_file, 'a') as fw:
        fw.write(caption.center(80, '-') + '\n')
        fw.write(payload + '\n')


def main():
    """main thread"""

    for ssh_host_info in pyexcel.get_sheet(file_name='hosts.xlsx'):
        t = threading.Thread(target=ssh_handler, args=ssh_host_info)
        t.start()


if __name__ == '__main__':
    main()
