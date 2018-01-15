# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from to_log import tolog
import time

Pass = "'result': 'p'"
Fail = "'result': 'f'"


class GUITestTool(object):

    def __init__(self, base_url="https://10.84.2.164/", user='administrator', password='password'):
        # mark test cases execution status
        self.FailFlag = False

        # configuration of Firefox for selenium
        browser_configuration = 'C:\Users\zach\AppData\Roaming\Mozilla\Firefox\Profiles\\bx7jnv81.selenium'

        # execution login
        self.driver = webdriver.Firefox(browser_configuration)
        self.driver.maximize_window()
        self.driver.get(base_url)
        self.driver.find_element_by_name("username").send_keys(user)
        self.driver.find_element_by_name("password").send_keys(password)
        self.click_action("//button[@type='submit']", 'login button')
        time.sleep(3)

    def finished(self):
        self.driver.close()

    """
    locator type: 
    By.ID,By.NAME,By.CLASS_NAME,By.TAG_NAME,By.LINK_TEXT,By.PARTIAL_LINK_TEXT,By.XPATH,By.CSS_SELECTOR
    """
    def click_action(self, locator, path, location='', response_time=3):

        try:
            self.driver.find_element(locator, path).click()
            time.sleep(response_time)
        except:
            tolog('to click ' + location + ' is failed\r\n')

    def fill_action(self, locator, path, value, location=''):

        try:
            self.driver.find_element(locator, path).clear()
            self.driver.find_element(locator, path).send_keys(value)
            time.sleep(1)
        except:
            tolog('to fill out ' + location + ' is failed\r\n')

    def element_text_assert(self, locator, path, location='', expected_text=''):

        try:
            actual_text = self.driver.find_element(locator, path).text
            if actual_text != expected_text:
                self.FailFlag = True
                tolog('Expected: ' + expected_text + '\r\nActual: ' + actual_text + '\r\n')
        except:
            tolog(location + ' is not found\r\n')

    def wait_for_element(self, locator, path, location=''):

        for i in range(10):
            try:
                if self.driver.find_element(locator, path):
                    break
            except:
                tolog(location + ' is not found\r\n')
                break
            time.sleep(1)
        else:
            tolog('time out')

        return

    def mark_status(self):

        if self.FailFlag:
            tolog(Fail)
        else:
            tolog(Pass)