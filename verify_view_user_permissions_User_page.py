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

class verify_view_user_permissions_User_page(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://10.84.2.164/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_verify_view_user_permissions_User_page(self):
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

        # verify user page permissions
        driver.find_element_by_xpath("//ul/li[5]/a/span").click()
        time.sleep(0.5)
        driver.find_element_by_xpath("//tr[2]/td[1]/input").click()
        time.sleep(3)

        result.append(testLinkAssertEnabled("//pr-button-bar/div/div/div/button[1]", True,
                                            "Pass: Change Password button is enabled",
                                            "Fail: Change Password button is disabled"))
        result.append(testLinkAssertEnabled("//pr-button-bar/div/div/div/button[2]", True,
                                            "Pass: Modify button is enabled",
                                            "Fail: Modify button is disabled"))
        result.append(testLinkAssertEnabled("//pr-button-bar/div/div/div/button[3]", False,
                                            "Pass: Delete button is disabled",
                                            "Fail: Delete button is enabled"))
        result.append(testLinkAssertEnabled("//pr-button-bar/div/div/div/button[4]", False,
                                            "Pass: Add New User button is disabled",
                                            "Fail: Add New User button is enabled"))

        driver.find_element_by_xpath("//pr-gear-button/div/a").click()

        if "Not Authorized" not in driver.find_element_by_xpath("//pr-gear-button/div/ul/li[1]/a").get_attribute("title"):
            tolog("Pass: Change Password option can be selected")
            result.append(True)
        else:
            tolog("Fail: Change Password option can not be selected")
            result.append(False)

        if "Not Authorized" not in driver.find_element_by_xpath("//pr-gear-button/div/ul/li[2]/a").get_attribute("title"):
            tolog("Pass: Modify option can be selected")
            result.append(True)
        else:
            tolog("Fail: Modify option can not be selected")
            result.append(False)

        if "Not Authorized" in driver.find_element_by_xpath("//pr-gear-button/div/ul/li[3]/a").get_attribute("title"):
            tolog("Pass: Delete option can not be selected")
            result.append(True)
        else:
            tolog("Fail: Delete option can be selected")
            result.append(False)

        if "Not Authorized" not in driver.find_element_by_xpath("//pr-gear-button/div/ul/li[4]/a").get_attribute("title"):
            tolog("Pass: Event Subscription option can be selected")
            result.append(True)
        else:
            tolog("Fail: Event Subscription option can not be selected")
            result.append(False)

        # View user change password
        tolog("View user change password")
        driver.find_element_by_xpath("//div/pr-button-bar/div/div/div/button[1]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//div/form/div[2]/div[1]/input").clear()
        driver.find_element_by_xpath("//div/form/div[2]/div[1]/input").send_keys("1")
        time.sleep(1)
        driver.find_element_by_xpath("//div/form/div[3]/div[1]/input").clear()
        driver.find_element_by_xpath("//div/form/div[3]/div[1]/input").send_keys("2")
        time.sleep(1)
        driver.find_element_by_xpath("//div/form/div[4]/div[1]/input").clear()
        driver.find_element_by_xpath("//div/form/div[4]/div[1]/input").send_keys("2")
        time.sleep(1)
        driver.find_element_by_xpath("//div/div[2]/div[2]/button[1]").click()

        if "successfully" in driver.find_element_by_xpath("//div[1]/div/div[4]/div/div/span").text:
            tolog("Pass: View user can change password successfully")
            result.append(True)
        else:
            tolog("Fail: View user can not change password")
            result.append(False)

        # change back to original password
        time.sleep(1)
        driver.find_element_by_xpath("//tr[2]/td[1]/input").click()
        time.sleep(1)
        driver.find_element_by_xpath("//div/pr-button-bar/div/div/div/button[1]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//div/form/div[2]/div[1]/input").clear()
        driver.find_element_by_xpath("//div/form/div[2]/div[1]/input").send_keys("2")
        time.sleep(1)
        driver.find_element_by_xpath("//div/form/div[3]/div[1]/input").clear()
        driver.find_element_by_xpath("//div/form/div[3]/div[1]/input").send_keys("1")
        time.sleep(1)
        driver.find_element_by_xpath("//div/form/div[4]/div[1]/input").clear()
        driver.find_element_by_xpath("//div/form/div[4]/div[1]/input").send_keys("1")
        time.sleep(1)
        driver.find_element_by_xpath("//div/div[2]/div[2]/button[1]").click()
        time.sleep(1)

        # View user modify display name
        tolog("View user modify display name")
        driver.find_element_by_xpath("//tr[2]/td[1]/input").click()
        time.sleep(1)
        driver.find_element_by_xpath("//pr-button-bar/div/div/div/button[2]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//div/form/div[3]/div[1]/input").clear()
        driver.find_element_by_xpath("//div/form/div[3]/div[1]/input").send_keys("TestModify")
        time.sleep(1)
        driver.find_element_by_xpath("//div/div[2]/div[2]/button[1]").click()

        if "successfully" in driver.find_element_by_xpath("//div[1]/div/div[4]/div/div/span").text:
            tolog("Pass: View user can modify display name successfully")
            result.append(True)
        else:
            tolog("Fail: View user can not modify display name")
            result.append(False)

        # Setting event subscription
        driver.find_element_by_xpath("//div/div[1]/div/ol/li[3]/a").click()
        time.sleep(1)
        driver.find_element_by_xpath("//div/div[2]/table[2]/tbody/tr[2]/td[8]/pr-gear-button/div/a/i").click()
        time.sleep(1)
        driver.find_element_by_xpath("//tr[2]/td[8]/pr-gear-button/div/ul/li[4]/a").click()
        time.sleep(1)
        driver.find_element_by_xpath("//div/form/div[3]/div/label/span").click()
        time.sleep(1)
        driver.find_element_by_xpath("//div/div[3]/div/div/div[2]/div[2]/button[1]").click()

        if "successfully" in driver.find_element_by_xpath("//div[1]/div/div[4]/div/div/span").text:
            tolog("Pass: View user can set Event Subscription")
            result.append(True)
        else:
            tolog("Fail: View user can not set Event Subscription")
            result.append(False)

        # mark result
        if result.count(True) != len(result):
            tolog('\n<font color="red">Fail: View user permissions is failed on User page </font>')
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
