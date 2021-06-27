#!/usr/bin/env python3
import click
import glob
import re
import sys


def get_system_file(name_fragment):
    glob_search = glob.glob(f'./**/{glob.escape(name_fragment)}', recursive=True)

    if not len(glob_search) or len(glob_search) > 1:
        print(f'System file from {name_fragment} found {glob_search}')
        return

    return glob_search[0]


def remove_console_logs(diff_lines, console_logs, console_log_files):
    for console_log_file in console_log_files:
        file_in_system = get_system_file(console_log_file)
        if not file_in_system:
            continue

        contents = ''
        with open(file_in_system, 'r') as f:
            contents = f.read()

            for console_log in console_logs:
                if console_log in contents and click.confirm(f'{file_in_system}\n{console_log.strip()} Delete?'):
                    contents = contents.replace((console_log + '\n'), '')
                    contents = contents.replace(console_log, '')

        with open(file_in_system, 'w') as f:
            f.write(contents)



def get_index_of_match(lines, match):
    for i, line in enumerate(lines):
        if re.search(re.escape(match), line):
            return i

    print(f'Could not find {match} in diff file.')


def find_git_files(lines, console_log_matches):
    files = []
    for match in console_log_matches:
        idx = get_index_of_match(lines, match)
        if not idx:
            continue

        for line in reversed(lines[:idx]):
            if re.search(r'\+\+\+ .+/', line): # git file
                files.append(line)
                break

    return [ '/'.join(x.strip().split('/')[-3:]) for x in files ]


def match_console_logs(lines):
    return re.findall(r'console\.log\(.*\);*', ''.join(lines))


def main(args):
    if len(args) < 2:
        print('Error')
        return

    time = args[1]
    with open(f'/Users/kkelso/logging/commit-diff-{time}.diff', 'r') as f:
        diff_lines = f.readlines()

        console_logs_in_diff = match_console_logs(diff_lines)

        if len(console_logs_in_diff) and click.confirm(f'Found {len(console_logs_in_diff)} console logs. Remove?'):
            console_log_files = find_git_files(diff_lines, console_logs_in_diff)
            remove_console_logs(diff_lines, console_logs_in_diff, console_log_files)


if __name__ == '__main__':
    main(sys.argv)

