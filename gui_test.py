# -*- coding: utf-8 -*-
from selenium import webdriver
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
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(3)

    def finished(self):
        self.driver.close()

    def click_action(self, path):
        self.driver.find_element_by_xpath(path).click()
        time.sleep(2)

    def fill_action(self, path, value):
        self.driver.find_element_by_xpath(path).clear()
        self.driver.find_element_by_xpath(path).send_keys(value)
        time.sleep(2)

    def wait_for_element(self, locator, path):

        for i in range(30):
            try:
                if self.driver.find_element(locator, path):
                    break
            except():
                pass
            time.sleep(1)
        else:
            tolog('time out')

        return

    def mark_status(self):

        if self.FailFlag:
            tolog(Fail)
        else:
            tolog(Pass)