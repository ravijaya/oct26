"""ftp client"""
from ftplib import FTP


def ftp_connect(host, user, pwd):
    """conntect to the ftp server"""
    ftp = FTP()
    ftp.connect(host)
    ftp.login(user, pwd)
    return ftp


def ftp_upload(ftp, file_name):
    cmd = f'STOR {file_name}'  # FTP Commands
    ftp.storbinary(cmd, open(file_name, 'rb'))
    print(f'{file_name}: uploaded')


def ftp_close(ftp):
    ftp.close()


if __name__ == '__main__':
    ftp_client = ftp_connect('13.235.81.161', 'training', 'training')
    name = 'passwd.txt'
    ftp_upload(ftp_client, name)
    ftp_close(ftp_client)
