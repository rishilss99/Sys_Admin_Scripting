#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    for idx, line in enumerate(sys.stdin):
        print(f"{idx}: {line}")