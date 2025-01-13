#!/usr/bin/env python3

import os
import Pyro4.core

@Pyro4.expose
class PyroExample(object):
    def ls(self, directory):
        try:
            return os.listdir(directory)
        except OSError:
            return []

    def ls_boom(self, directory):
        return os.listdir(directory)

    def cb(self, obj):
        print("OBJECT::", obj)
        print("OBJECT::__class__::", obj.__class__)
        return obj.cb()
    
if __name__ == "__main__":
    host = "127.0.0.1"
    port = 5555
    daemon = Pyro4.Daemon(host=host, port=port)
    
    uri = daemon.register(PyroExample)
    print(f"Server is running. Access URI: {uri}")

    # Start the server loop
    daemon.requestLoop()
