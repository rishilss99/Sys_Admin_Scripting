#!/usr/bin/env python3
"""
    Usage: ./filesystem_walk.py -d/--dir directory_name
"""

import os
from optparse import OptionParser

def walkDir(directory):
    paths = []
    dir_name = os.path.abspath(directory)
    for dirpath, dirnames, filenames in os.walk(dir_name):
        for file in filenames:
            paths.append(os.path.join(dir_name, dirpath, file))
    return paths

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-d", "--dir", dest="directory", help="Walk FILE path", metavar="FILE")
    (options, args) = parser.parse_args()
    if not options.directory:
        print(__doc__)
        exit(1)
    if not (os.path.exists(options.directory) and os.path.isdir(options.directory)):
        print(__doc__)
        exit(1)
    print("\nRecursive listing of all paths in a dir:")
    paths = walkDir(options.directory)
    for path in paths:
        print(path)
