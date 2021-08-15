#!/usr/bin/env python3

import sys

def main(message):
    lines = []
    with open('commitMsgs.txt', 'r') as f:
        lines = f.readlines()

    print(lines)
    if message not in lines:
        print('writing')
        with open('commitMsgs.txt', 'a') as f:
            f.write(message)

if __name__ == '__main__':
    print(sys.argv)
    if len(sys.argv) != 2:
        exit(1)

    main(sys.argv[1])

