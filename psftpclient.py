from ftplib import FTP


# from psmarkearchive import make_archive, glob


def ftp_connect(host, user, pwd):
    ftp = FTP()
    ftp.connect(host)
    ftp.login(user, pwd)
    return ftp


def ftp_upload(ftp, file_name):
    cmd = f'STOR {file_name}'
    ftp.storbinary(cmd, open(file_name, 'rb'))
    print(f'{file_name}: uploaded')


if __name__ == '__main__':
    ftp = ftp_connect('localhost', 'training', 'training')
    name = 'content.zip'
    # make_archive(name, *glob('*.*'))
    ftp_upload(ftp, name)
