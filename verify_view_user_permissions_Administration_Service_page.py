# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from to_log import tolog
from precondition import *
from clearUP import *
import unittest, time, re

Pass = "'result': 'p'"
Fail = "'result': 'f'"

class verify_view_user_permissions_Administration_Service_page(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://10.84.2.164/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_verify_view_user_permissions_Administration_Service_page(self):
        driver = self.driver
        result = []

        def testLinkAssertEnabled(element, expected, TrueTolog, FalseTolog):
            if driver.find_element_by_xpath(element).is_enabled() == expected:
                tolog(TrueTolog)
                return True
            else:
                tolog(FalseTolog)
                return False

        driver.get(self.base_url + "/")
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("a")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("1")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        for i in range(60):
            try:
                if self.is_element_present(By.XPATH, "//div[2]/div/h4"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")

        # verify Administration page permissions
        driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/ul/li[7]/a/span").click()
        time.sleep(1)

        # Service
        tolog("Service")
        driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div/div[1]/div/ul/li[2]/a/span/span").click()
        time.sleep(1)

        type = ['Email', 'SLP', 'Webserver', 'SSH', 'SNMP', 'Redis']

        for i in range(0, 5):
            driver.find_element_by_xpath("//tr[" + str(2 + i) + "]/td[4]/pr-gear-button/div/a/i").click()
            time.sleep(3)

            if "Not Authorized" in driver.find_element_by_xpath("//tr[2]/td[4]/pr-gear-button/div/ul/li[1]/a").get_attribute("title"):
                tolog("Pass: " + type[i] + "-Start option can not be selected")
                result.append(True)
            else:
                tolog("Fail: " + type[i] + "-Start option can be selected")
                result.append(False)

            if "Not Authorized" in driver.find_element_by_xpath("//tr[2]/td[4]/pr-gear-button/div/ul/li[2]/a").get_attribute("title"):
                tolog("Pass: " + type[i] + "-Stop option can not be selected")
                result.append(True)
            else:
                tolog("Fail: " + type[i] + "-Stop option can be selected")
                result.append(False)

            if "Not Authorized" in driver.find_element_by_xpath("//tr[2]/td[4]/pr-gear-button/div/ul/li[3]/a").get_attribute("title"):
                tolog("Pass: " + type[i] + "-Restart option can not be selected")
                result.append(True)
            else:
                tolog("Fail: " + type[i] + "-Restart option can be selected")
                result.append(False)

            if "Not Authorized" in driver.find_element_by_xpath("//tr[2]/td[4]/pr-gear-button/div/ul/li[4]/a").get_attribute("title"):
                tolog("Pass: " + type[i] + "-Settings option can not be selected")
                result.append(True)
            else:
                tolog("Fail: " + type[i] + "-Settings option can be selected")
                result.append(False)

            if type[i] == 'SSH':
                if "Not Authorized" in driver.find_element_by_xpath("//tr[2]/td[4]/pr-gear-button/div/ul/li[5]/a").get_attribute("title"):
                    tolog("Pass: " + type[i] + "-SSH Public Key Management option can not be selected")
                    result.append(True)
                else:
                    tolog("Fail: " + type[i] + "-SSH Public Key Management option can be selected")
                    result.append(False)

            if type[i] == 'SNMP':
                if "Not Authorized" in driver.find_element_by_xpath("//tr[2]/td[4]/pr-gear-button/div/ul/li[5]/a").get_attribute("title"):
                    tolog("Pass: " + type[i] + "-Set Security User option can not be selected")
                    result.append(True)
                else:
                    tolog("Fail: " + type[i] + "-Set Security User option can be selected")
                    result.append(False)

            driver.find_element_by_xpath("//pr-page-header/div/div/div[1]/h3").click()
            time.sleep(0.5)

        if result.count(True) != len(result):
            tolog('\n<font color="red">Fail: View user permissions is failed on Administrator_Service page </font>')
            tolog(Fail)
        else:
            tolog('\n<font color="green">Pass</font>')
            tolog(Pass)

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
