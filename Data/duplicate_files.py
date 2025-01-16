#!/usr/bin/env python3
"""
    Python script to find duplicate files in given directory
    Usage: ./duplicate_files.py -d/--dir directory_name
"""

import file_md5sum
import filesystem_walk
import os

def findDuplicateFiles(path):
    dup = []
    records = {}
    for file in filesystem_walk.walkDir(path):
        compound_key = (os.path.getsize(file), file_md5sum.fileChecksum(file))
        if compound_key in records:
            dup.append(file)
        else:
            records[compound_key] = file
    return dup

if __name__ == "__main__":
    from optparse import OptionParser
    parser = OptionParser()

    parser.add_option("-d", "--dir", dest="directory", help="Walk FILE path", metavar="FILE")
    (options, args) = parser.parse_args()
    if not options.directory:
        print(__doc__)
        exit(1)
    if not (os.path.exists(options.directory) and os.path.isdir(options.directory)):
        print(__doc__)
        exit(1)
    print(findDuplicateFiles(options.directory))