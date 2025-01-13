#!/usr/bin/env python3

import ftplib
from ftplib import FTP
from optparse import OptionParser
import sys

def retrieveRemoteFile(remote_address, remote_file, local_file, username = None, password = None):
    ftp = FTP(remote_address)
    if username:
        try:
            ftp.login(username, password)
        except ftplib.error_perm as e:
            print(f"Login failed: {e}")
            sys.exit(1)
    else:
        try:
            ftp.login()
        except ftplib.error_perm as e:
            print(f"Anonymous login failed: {e}")
            sys.exit(1)
    try:
        local_f = open(local_file, "wb")
        ftp.retrbinary("RETR %s" % remote_file, local_f.write)
    finally:
        local_f.close()
        ftp.close()

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-a", "--remote_host_address", dest="remote_host_address",
                      help="REMOTE FTP HOST.", metavar="REMOTE FTP HOST")
    parser.add_option("-r", "--remote_file", dest="remote_file",
                      help="REMOTE FILE NAME to download.", metavar="REMOTE FILE NAME")
    parser.add_option("-l", "--local_file", dest="local_file",
                      help="LOCAL FILE NAME to save remote file to", metavar="LOCAL FILE NAME")
    parser.add_option("-u", "--username", dest="username",
                      help="USERNAME for ftp server", metavar="USERNAME")
    parser.add_option("-p", "--password", dest="password",
                      help="PASSWORD for ftp server", metavar="PASSWORD")
    
    (options, args) = parser.parse_args()
    if not (options.remote_file and options.local_file and options.remote_host_address):
        parser.error('REMOTE HOST, LOCAL FILE NAME, ' \
                    'and REMOTE FILE NAME are mandatory')
    if options.username and not options.password:
        parser.error('PASSWORD is mandatory if USERNAME is present')

    retrieveRemoteFile(options.remote_host_address, options.remote_file, options.local_file, options.username, options.password)