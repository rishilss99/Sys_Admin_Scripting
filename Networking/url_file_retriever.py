#!/usr/bin/env python3
"""
url retriever

Usage:
url_retrieve_urllib.py URL FILENAME

URL:
If the URL is an FTP URL the format should be:
ftp://[username[:password]@]hostname/filename
If you want to use absolute paths to the file to download,
you should make the URL look something like this:
ftp://user:password@host/%2Fpath/to/myfile.txt
Notice the '%2F' at the beginning of the path to the file.

FILENAME:
absolute or relative path to the filename to save downloaded file as
"""

import sys
import urllib
import urllib.request

if __name__ == "__main__":
    if "-h" in sys.argv or "--help" in sys.argv:
        print(__doc__)
        exit(1)

    if not len(sys.argv) == 3:
        print(__doc__)
        exit(1)
    
    url = sys.argv[1]
    filename = sys.argv[2]
    print(urllib.request.urlretrieve(url, filename))
    urllib.request.urlretrieve()