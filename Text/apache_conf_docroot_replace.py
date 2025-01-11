#!/usr/bin/env python3

import re

vhost_start = re.compile(r"<VirtualHost\s+(.*?)>")
doc_root = re.compile(r"(DocumentRoot\s+)(\S+)")
vhost_end = re.compile(r"</VirtualHost>")

def docroot_replace(conf_file, vhost, new_docroot):
    in_vhost = False
    curr_vhost = None
    for line in conf_file:
        vhost_start_match = vhost_start.search(line)
        if vhost_start_match:
            curr_vhost = vhost_start_match.groups()[0]
            in_vhost = True
        if in_vhost and (curr_vhost == vhost):
            doc_root_match = doc_root.search(line)
            if doc_root_match:
                sub_line = doc_root.sub(r"\1%s" % new_docroot,line)
                line = sub_line
        vhost_end_match = vhost_end.search(line)
        if vhost_end_match:
            in_vhost = False
        yield line

if __name__ == "__main__":
    import sys
    file = sys.argv[1]
    vhost = sys.argv[2]
    docroot = sys.argv[3]
    infile = open(file, "r")
    for line in docroot_replace(infile, vhost, docroot):
        print(line, end="")

