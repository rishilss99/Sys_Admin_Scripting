#!/usr/bin/env python3

import hashlib

def fileChecksum(path):
    """
    Reads in file. Creates checksum of entire file
    """
    f = open(path, "rb")
    checksum = hashlib.md5()
    while True:
        buffer = f.read(8192)
        if not buffer:
            break
        checksum.update(buffer)
    f.close()
    return checksum.hexdigest()