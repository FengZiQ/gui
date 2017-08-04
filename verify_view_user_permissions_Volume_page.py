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

class verify_view_user_permissions_Volume_page(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://10.84.2.164/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_verify_view_user_permissions_Volume_page(self):
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

        # precondition
        c, ssh = ssh_conn()
        createPool(c)
        createVolume(c)
        time.sleep(3)

        # verify volume page permissions
        driver.find_element_by_link_text("Volume").click()
        for i in range(60):
            try:
                if self.is_element_present(By.XPATH, "//tr[2]/td[2]"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")

        driver.find_element_by_xpath("//tr[2]/td[1]/input").click()
        time.sleep(3)

        result.append(testLinkAssertEnabled("//div[1]/div/div[2]/button", False,
                                            "Pass: Create New Volume button is disabled",
                                            "Fail: Create New Volume button is enabled"))
        result.append(testLinkAssertEnabled("//pr-button-bar/div/div/div/button[1]", False,
                                            "Pass: Delete button is disabled",
                                            "Fail: Delete button is enabled"))
        result.append(testLinkAssertEnabled("//pr-button-bar/div/div/div/button[2]", False,
                                            "Pass: Export button is disabled",
                                            "Fail: Export button is enabled"))
        result.append(testLinkAssertEnabled("//pr-button-bar/div/div/div/button[3]", False,
                                            "Pass: Un-export button is disabled",
                                            "Fail: Un-export button is enabled"))

        driver.find_element_by_xpath("//pr-gear-button/div/a/i").click()
        time.sleep(3)

        if "Not Authorized" not in driver.find_element_by_xpath("//tr[2]/td[9]/pr-gear-button/div/ul/li[1]/a").get_attribute("title"):
            tolog("Pass: View option Detail can be selected")
            result.append(True)
        else:
            tolog("Fail: View Detail option can not be selected")
            result.append(False)

        if "Not Authorized" in driver.find_element_by_xpath("//tr[2]/td[9]/pr-gear-button/div/ul/li[2]/a").get_attribute("title"):
            tolog("Pass: Delete option can not be selected")
            result.append(True)
        else:
            tolog("Fail: Delete option can be selected")
            result.append(False)

        if driver.find_element_by_xpath("//div/div[1]/table[2]/tbody/tr[2]/td[6]").text == "Exported":
            if "Not Authorized" in driver.find_element_by_xpath("//tr[2]/td[9]/pr-gear-button/div/ul/li[4]/a").get_attribute("title"):
                tolog("Pass: Un-Exported option can not be selected")
                result.append(True)
            else:
                tolog("Fail: Un-Exported option can be selected")
                result.append(False)
        elif driver.find_element_by_xpath("//div/div[1]/table[2]/tbody/tr[2]/td[6]").text == "Un-Exported":
            if "Not Authorized" in driver.find_element_by_xpath("//tr[2]/td[9]/pr-gear-button/div/ul/li[3]/a").get_attribute("title"):
                tolog("Pass: Exported option can not be selected")
                result.append(True)
            else:
                tolog("Fail: Exported option can be selected")
                result.append(False)

        if "Not Authorized" not in driver.find_element_by_xpath("//pr-gear-button/div/ul/li[5]/a").get_attribute("title"):
            tolog("Pass: Snapshot & Clone option can be selected")
            result.append(True)
        else:
            tolog("Fail: Snapshot & Clone option can not be selected")
            result.append(False)

        if result.count(True) != len(result):
            tolog('\n<font color="red">Fail: View user permissions is failed on volume page </font>')
            tolog(Fail)
        else:
            tolog('\n<font color="green">Pass</font>')
            tolog(Pass)

        clearUpPool(c)
        ssh.close()

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
