#!/usr/bin/env python3

import os
import filesystem_walk
import re
from fnmatch import fnmatch

def renameFiles(directory = ".", src_ext = "txt", dst_ext = "text"):
    re_obj = re.compile(rf"/(\w+)\.({src_ext})")
    for file in filesystem_walk.walkDir(directory):
        if fnmatch(file, f"*.{src_ext}"):
            new = re_obj.sub(rf"/\1.{dst_ext}", file)
            os.rename(file, new)
            print(new)

if __name__ == "__main__":
    renameFiles()
