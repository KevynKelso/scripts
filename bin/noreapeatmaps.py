#!/usr/bin/env python3

import re

MAPS_FILE_PATH = '/Users/kkelso/Desktop/projects/vim_config/nvim/plugin/maps.vim'

def check_duplicates(mappings, mode):
    ''' Check if given list contains any duplicates '''
    for elem, m in zip(mappings, mode):
        if mappings.count(elem) > 1:
            # TODO: check that the mode is not different
            print(f'Duplicate mapping: {elem}')

def get_mappings_and_mode(content_lines):
    mappings = []
    modes = []
    for line in content_lines:
        if not re.search('^[ntvix]', line):
            continue

        modes.append(line.split(' ')[0]
        mappings.append(line.split(' ')[1])

    return mappings, modes

def main():
    content_lines =[]
    with open(MAPS_FILE_PATH, 'r') as f:
        content_lines = f.readlines()

    mappings, modes = get_mappings_and_mode(content_lines)
    check_duplicates(mappings, mode)


if __name__ == '__main__':
    main()

