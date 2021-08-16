#!/usr/bin/env python3
COMMIT_MSGS_PATH = '/Users/kkelso/Desktop/projects/scripts/bin/commitMsgs.txt'

import sys

def main(message):
    if message == '':
        return

    lines = []
    with open(COMMIT_MSGS_PATH, 'r') as f:
        lines = f.readlines()

    if message not in lines:
        with open(COMMIT_MSGS_PATH, 'a') as f:
            f.write(message)

if __name__ == '__main__':
    main(sys.stdin.read())
