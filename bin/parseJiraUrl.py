#!/usr/bin/env python3

import sys

def main(args):
    if len(args) < 1:
        return ""

    url = args[1]
    slices = url.split("-")
    if len(slices) < 2:
        return ""

    # should be ticket number
    return slices[1]

if __name__ == '__main__':
    print(main(sys.argv))

