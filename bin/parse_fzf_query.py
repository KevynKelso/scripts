#!/usr/bin/env python3

import sys

if __name__ == '__main__':
    if len(sys.argv) == 1 or len(sys.argv) > 3:
        exit(1)

    if len(sys.argv) == 3:
        print(sys.argv[2])

    if len(sys.argv) == 2:
        print(sys.argv[1])
