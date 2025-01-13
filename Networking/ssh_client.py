#!/usr/bin/env python3

import paramiko
import paramiko.util

hostname = "127.0.0.1"
port = 22
user = "rishah"
password = "3004"

def getIfConfig():
    paramiko.util.log_to_file("ssh.log")
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname, port, user, password)
    stdin, stdout, stderr = s.exec_command('ifconfig')
    print(stdout.read().decode("utf-8"))
    s.close()

def getDirListSFTP():
    transport = paramiko.Transport((hostname, port))
    transport.connect(username=user, password=password)
    sftp = paramiko.SFTPClient.from_transport(transport)
    files = sftp.listdir("/home/rishah/python_unix/Networking")
    for i in files:
        print(i)
    transport.close()

if __name__ == "__main__":
    getDirListSFTP()