#!/usr/bin/env python3

import sys
import time
import logging
import os

from selenium import webdriver
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

browser = webdriver.Chrome()
browser.set_window_position(0,0)
quit_options = ['q', 'quit', 'exit', 'stop']
log_dir = '/Users/kkelso/logging'
identifier_delim = '*****'

def stop():
    browser.quit()
    os.remove(f'{log_dir}/autoSearch.txt')
    sys.exit(0)


def on_modified(event):
    with open(f'{log_dir}/autoSearch.txt', 'r') as f:
        search_string = f.read().split(identifier_delim)[-1]
        print(search_string)

        if search_string in quit_options:
            stop()

    browser.get(f'https://www.google.com/search?q={search_string}')

def event_handler():
    patterns = ['*']
    ignore_patterns = None
    ignore_dirs = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_dirs, case_sensitive)
    my_event_handler.on_modified = on_modified
    return my_event_handler


def main(stdin):
    my_event_handler = event_handler()

    my_observer = Observer()
    my_observer.schedule(my_event_handler, log_dir, recursive=False)
    my_observer.start()
    print(f'autoSearch running. Watching {log_dir}')
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        my_observer.stop()
        my_observer.join()

if __name__ == '__main__':
    main(sys.stdin)
