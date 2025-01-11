#!/usr/bin/env python3

import shelve
import apache_log_parser_regex

if __name__ == "__main__":
    logfile = open("apache.log", "r")
    shelvefile = shelve.open("access.s")

    for line in logfile:
        d = apache_log_parser_regex.dictify_logline(line)
        print(d)
        shelvefile[d['remote_host']] = shelvefile.setdefault(d['remote_host'], 0) + int(d['bytes_sent'])

    logfile.close()
    shelvefile.close()