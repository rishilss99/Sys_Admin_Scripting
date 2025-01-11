#!/usr/bin/env python3

import docutils.core

if __name__ == "__main__":

    server_list = '''
    ============== ============ ================
      Server Name   IP Address      Function
    ============== ============ ================
    card           192.168.1.2  mail server
    vinge          192.168.1.4  web server
    asimov         192.168.1.8  database server
    stephenson     192.168.1.16 file server
    gibson         192.168.1.32 print server
    ============== ============ ================'''

    html = docutils.core.publish_string(source = server_list, writer_name = 'html')
    
    print(html[html.find("<body>".encode("utf-8")) + 6: html.find("</body>".encode("utf-8"))].decode('utf-8'))