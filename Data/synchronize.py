#!/usr/bin/env python3
"""
Wrapper for rsync
Usage: python3 synchronize.py -s/--src dir_a -d/--dst dir_b
"""

import subprocess
import sys
import time
from optparse import OptionParser
import os

def sync(src, dest):
    flags = "-av"
    rsync = "rsync"
    command = f"{rsync} {flags} {src}/ {dest}"
    while True:
        ret = subprocess.call(command, shell = True)
        if ret != 0:
            print("Resubmitting rsync")
            time.sleep(30)
        else:
            print("Rsync successful")
            sys.exit(0)

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-s", "--src", dest="src", help="Source directory", metavar="SRC")
    parser.add_option("-d", "--dst", dest="dst", help="Destination directory", metavar="DST")
    (options, args) = parser.parse_args()
    if not (options.src and options.dst):
        print(__doc__)
        exit(1)
    if not (os.path.exists(options.src) and os.path.isdir(options.src)):
        print(__doc__)
        exit(1)
    if not (os.path.exists(options.dst) and os.path.isdir(options.dst)):
        print(__doc__)
        exit(1)
    sync(options.src, options.dst)
