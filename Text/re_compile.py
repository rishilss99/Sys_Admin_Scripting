#!/usr/bin/env python3
import re

def re_no_compile():
    
    pattern = "^Vm"
    file = open("/proc/meminfo")

    match_count = 0
    lines = 0

    for l in file:
        match = re.search(pattern, l)
        if match:
            match_count += 1
        lines += 1
    
    file.close()
    return (lines, match_count)

def re_compile():
    
    pattern = "^Vm"
    re_obj = re.compile(pattern)
    file = open("/proc/meminfo")

    match_count = 0
    lines = 0

    for l in file:
        match = re_obj.search(l)
        if match:
            match_count += 1
        lines += 1
    
    file.close()
    return (lines, match_count)


if __name__ == "__main__":
    lines, match_count = re_compile()
    print('LINES::', lines)
    print('MATCHES::', match_count)