#!/usr/bin/env python3

import sys

if __name__ == '__main__':
    input_lines = []
    for line in sys.stdin:
        input_lines.append(line.strip())

    print(list(filter(None, input_lines))[-1])
