#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time
import socket


def start():
    delay = 60
    browser = webdriver.Chrome()

    while True:
        try:
            browser.get(f'http://localhost:8080')
        except:
            time.sleep(3)
            continue
        else:
            #the rest of the code
            break

    WebDriverWait(browser, delay).until(EC.element_to_be_clickable((By.ID, 'sidetab-arrow'))).click()

    time.sleep(1)

    file_upload = WebDriverWait(browser, delay).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='application--wrap']/div[@id='gesture-wrapper']/div[@id='appcontainer']/aside[@class='v-navigation-drawer v-navigation-drawer--absolute v-navigation-drawer--open v-navigation-drawer--temporary theme--light']/div[@class='v-tabs']/div[@class='v-window']/div[@class='v-window__container']/div[@id='syncydink']/div[@class='layout sidebar-form column']/div[@class='flex'][1]/div[2]/div[@class='v-input v-text-field v-text-field--single-line theme--light']/div[@class='v-input__control']/div[@class='v-input__slot']/div[@class='v-text-field__slot']/input")))
    file_upload.click()

    link = WebDriverWait(browser, delay).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='application--wrap']/div[@id='gesture-wrapper']/div[@id='appcontainer']/aside[@class='v-navigation-drawer v-navigation-drawer--absolute v-navigation-drawer--open v-navigation-drawer--temporary theme--light']/div[@class='v-tabs']/div[@class='v-tabs__bar theme--light']/div[@class='v-tabs__wrapper']/div[@class='v-tabs__container']/div[@class='v-tabs__div'][2]/a[@class='v-tabs__item']")))
    link.click()

    link = WebDriverWait(browser, delay).until(EC.element_to_be_clickable((By.ID, 'ConnectLocalButton'))).click()

    # find bt elements
    link = WebDriverWait(browser, delay).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='application--wrap']/div[@id='gesture-wrapper']/div[@id='appcontainer']/aside[@class='v-navigation-drawer v-navigation-drawer--absolute v-navigation-drawer--open v-navigation-drawer--temporary theme--light']/div[@class='v-tabs']/div[@class='v-window']/div[@class='v-window__container']/div[@id='buttplugpanel']/div[@id='buttplug-panel']/div[@class='layout column'][2]/div[@class='flex'][2]/button[@class='v-btn theme--light']")))
    link.click()

    # click on fleshlight launch selection
    link = WebDriverWait(browser, delay).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='application--wrap']/div[@id='gesture-wrapper']/div[@id='appcontainer']/aside[@class='v-navigation-drawer v-navigation-drawer--absolute v-navigation-drawer--open v-navigation-drawer--temporary theme--light']/div[@class='v-tabs']/div[@class='v-window']/div[@class='v-window__container']/div[@id='buttplugpanel']/div[@id='buttplug-panel']/div[@class='layout column'][2]/div[@class='flex'][1]/div[@class='v-input v-input--selection-controls v-input--checkbox theme--light']/div[@class='v-input__control']/div[@class='v-input__slot']/div[@class='v-input--selection-controls__input']/div[@class='v-input--selection-controls__ripple']")))
    link.click()

    link = WebDriverWait(browser, delay).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='application--wrap']/div[@id='gesture-wrapper']/div[@id='appcontainer']/aside[@class='v-navigation-drawer v-navigation-drawer--absolute v-navigation-drawer--open v-navigation-drawer--temporary theme--light']/div[@class='v-tabs']/div[@class='v-tabs__bar theme--light']/div[@class='v-tabs__wrapper']/div[@class='v-tabs__container']/div[@class='v-tabs__div'][1]/a[@class='v-tabs__item']")))
    link.click()

    file_upload = WebDriverWait(browser, delay).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='application--wrap']/div[@id='gesture-wrapper']/div[@id='appcontainer']/aside[@class='v-navigation-drawer v-navigation-drawer--absolute v-navigation-drawer--open v-navigation-drawer--temporary theme--light']/div[@class='v-tabs']/div[@class='v-window']/div[@class='v-window__container']/div[@id='syncydink']/div[@class='layout sidebar-form column']/div[@class='flex'][2]/div[2]/div[@class='v-input v-text-field v-text-field--single-line theme--light']")))
    file_upload.click()

    link = WebDriverWait(browser, delay).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='application--wrap']/div[@id='gesture-wrapper']/div[@id='appcontainer']/aside[@class='v-navigation-drawer v-navigation-drawer--absolute v-navigation-drawer--open v-navigation-drawer--temporary theme--light']/div[@class='v-tabs']/div[@class='v-window']/div[@class='v-window__container']/div[@id='syncydink']/div[@class='layout sidebar-form column']/div[@class='flex'][2]/div[@class='v-input v-input--selection-controls v-input--checkbox theme--light']/div[@class='v-input__control']/div[@class='v-input__slot']")))
    link.click()

    q = input("quit?")

    browser.quit()


def main():
    start()


if __name__ == '__main__':
    main()

