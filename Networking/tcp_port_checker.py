#!/usr/bin/env python3

import socket
import sys

def checkServer(address, port):
    """Checks whether server is up and running."""
    s = socket.socket()
    print(f"Attempting to connect to {address} on port {port}")
    try:
        s.connect((address, port))
        print("Connected")
        return True
    except socket.error as e:
        print(f"Connection failed with: {e}")
        return False
    
if __name__ == "__main__":
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("-a", "--address", dest = "address", default = "localhost",
                      help = "ADDRESS for server", metavar = "ADDRESS")
    parser.add_option("-p", "--port", dest = "port", type = int, default = 80,
                      help = "PORT for server", metavar = "PORT")
    (options, args) = parser.parse_args()
    print(f"Options: {options}, Args: {args}")
    check = checkServer(options.address, options.port)
    print("Check server return %s" % check)
    sys.exit(not check)
