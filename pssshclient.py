"""single threaded ssh client"""

import paramiko


def ssh_client(host, port, user, pwd, job):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port, user, pwd)

    stdin, stdout, stderr = ssh.exec_command(job)

    output = stdout.read()
    response = output if output else stderr.read()  # if else conditional operator
    ssh.close()
    return response.decode()


if __name__ == '__main__':
    r = ssh_client('52.66.251.190', '22', 'training', 'training', 'lscpu')
    print(r)
