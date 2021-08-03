#!/usr/bin/env python3

import socket
import time
import sys

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

PORT = 10004

def search_web(browser, msg):
    browser.get(f'https://www.google.com/search?q={msg}')
    link = WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "h3")))
    link.click()


def get_tcp_message(s):
    clientsocket, _ = s.accept()

    return clientsocket.recv(1024).decode("utf-8"), clientsocket


def initialize_browser():
    browser = webdriver.Chrome()
    browser.set_window_position(0,0)

    return browser


def get_tcp_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    location = ('', PORT)
    s.bind(location)
    s.listen(10) # queue of 10, don't need it that big, but just in case

    return s


def main():
    s = get_tcp_socket()
    browser = initialize_browser()

    while True:
        msg, clientsocket = get_tcp_message(s)
        clientsocket.close()

        if msg.strip() == 'q':
            break

        try:
            search_web(browser, msg)
        except Exception as e:
            print(e)

    s.close()
    browser.quit()


if __name__ == '__main__':
    main()

