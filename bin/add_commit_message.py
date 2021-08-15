#!/usr/bin/env python3

import sys

def main(message):
    lines = []
    with open('commitMsgs.txt', 'r') as f:
        lines = f.readlines()

    if message not in lines:
        with open('commitMsgs.txt', 'a') as f:
            f.write(message)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        exit(1)

    main(sys.argv[1])
