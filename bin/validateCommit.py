#!/usr/bin/env python3

import sys

def checkContainsType(message):
    if ':' not in message:
        return False

    valid_types = ['feat', 'fix', 'chore', 'docs', 'BREAKING CHANGE']
    for t in valid_types:
        if t in message:
            return True

    return False


def main(args):
    if len(args) < 1:
        return "error"

    message = args[1]
    if checkContainsType(message) == False:
        return "not-valid"

    return "valid"

if __name__ == '__main__':
    print(main(sys.argv))
