#!/usr/bin/env python3

import re
import sys

def main():
    if len(sys.argv) < 2:
        return "invalid"

    git_data = sys.argv[1]

    m = re.search(r'HEAD branch: (\w+)', git_data)
    if m:
        return m.group(1)

    return "Match not found, git may have updated"

if __name__ == '__main__':
    print(main())

