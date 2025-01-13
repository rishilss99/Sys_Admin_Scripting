#!/usr/bin/env python3

import sys
import http.client

def checkWebServer(address, port, resource):
    """Checks if given server is available and has the mentioned resource."""
    if not resource.startswith('/'):
        resource = '/' + resource
    try:
        conn = http.client.HTTPConnection(address, port)
        conn.request("GET", resource)
        print("Request successful for %s" % resource)
        resp = conn.getresponse()
        print("Response status: %d" % resp.status)
    except ConnectionRefusedError as e:
        print("HTTP connection failed: %s" % e)
        return False
    except http.client.RemoteDisconnected as e:
        conn.close()
        print("Remote Disconnected without response: %s" % e)
        return False
    finally:
        conn.close()
        print("HTTP Connection closed successfully")
    if resp.status in [200, 301]:
        return True
    else:
        return False

if __name__ == "__main__":
    from optparse import OptionParser

    parser = OptionParser()
    parser.add_option("-a", "--address", dest="address", default="localhost",
                      help="ADDRESS for webserver", metavar="ADDRESS")
    parser.add_option("-p", "--port", dest="port", type=int, default=80,
                      help="PORT for webserver", metavar="PORT")
    parser.add_option("-r", "--resource", dest="resource", default="index.html",
                      help="RESOURCE for webserver", metavar="RESOURCE")
    (options, args) = parser.parse_args()
    print(f"Options: {options}, Args: {args}")
    check = checkWebServer(options.address, options.port, options.resource)
    sys.exit(not check)   


    