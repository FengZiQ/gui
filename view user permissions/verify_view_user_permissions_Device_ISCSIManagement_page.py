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

class verify_view_user_permissions_Device_ISCSIManagement_page(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://10.84.2.164/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_verify_view_user_permissions_Device_ISCSIManagement_page(self):
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
        createCHAP(c)
        time.sleep(3)

        # verify Device page permissions
        driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/ul/li[6]/a/span").click()
        time.sleep(3)

        # ISCSI Management
        tolog("ISCSI Management")
        # Target
        tolog("Target")
        driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div/div[1]/div/ul/li[9]/a/i").click()
        time.sleep(1)
        for i in range(60):
            try:
                if self.is_element_present(By.XPATH,"/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div/div[1]/div/ul/li[9]/ul/li[5]/a/span/span"):
                    driver.find_element_by_xpath("html/body/div[1]/div/div[3]/div[1]/div/div[2]/div/div[1]/div/ul/li[9]/ul/li[1]/a/span/span").click()
                    break
            except:
                pass
            time.sleep(1)
        else:
            driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div/div[1]/div/ul/li[9]/a/i").click()

        time.sleep(1)

        result.append(testLinkAssertEnabled("//pr-button-bar/div/div/div/button", False,
                                            "Pass: Target-Modify button is disabled",
                                            "Fail: Target-Modify button is enabled"))

        # ISNS
        tolog("ISNS")
        for i in range(60):
            try:
                if self.is_element_present(By.XPATH,"/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div/div[1]/div/ul/li[9]/ul/li[5]/a/span/span"):
                    driver.find_element_by_xpath("html/body/div[1]/div/div[3]/div[1]/div/div[2]/div/div[1]/div/ul/li[9]/ul/li[3]/a/span/span").click()
                    break
            except:
                pass
            time.sleep(1)
        else:
            driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div/div[1]/div/ul/li[9]/a/i").click()

        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[2]/div/div/div[2]/div/div/table[2]/tbody/tr[2]/td[1]/input").click()
        time.sleep(1)

        result.append(testLinkAssertEnabled("//pr-button-bar/div/div/div/button", False,
                                            "Pass: ISNS-Modify button is disabled",
                                            "Fail: ISNS-Modify button is enabled"))

        # CHAP
        tolog("CHAP")
        createCHAP(c)
        time.sleep(3)
        for i in range(60):
            try:
                if self.is_element_present(By.XPATH,"/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div/div[1]/div/ul/li[9]/ul/li[5]/a/span/span"):
                    driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div/div[1]/div/ul/li[9]/ul/li[4]/a/span/span").click()
                    break
            except:
                pass
            time.sleep(1)
        else:
            driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div/div[1]/div/ul/li[9]/a/i").click()

        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[2]/div/div/div[2]/div/div/table[2]/tbody/tr[2]/td[1]/input").click()
        time.sleep(3)

        result.append(testLinkAssertEnabled("//pr-button-bar/div/div/div/button[1]", False,
                                            "Pass: CHAP-Modify button is disabled",
                                            "Fail: CHAP-Modify button is enabled"))
        result.append(testLinkAssertEnabled("//pr-button-bar/div/div/div/button[2]", False,
                                            "Pass: CHAP-Modify button is disabled",
                                            "Fail: CHAP-Modify button is enabled"))
        result.append(testLinkAssertEnabled("//pr-button-bar/div/div/div/button[3]", False,
                                            "Pass: CHAP-Modify button is disabled",
                                            "Fail: CHAP-Modify button is enabled"))

        driver.find_element_by_xpath("//tr[2]/td[5]/pr-gear-button/div/a/i").click()
        time.sleep(1)

        if "Not Authorized" in driver.find_element_by_xpath("//tr[2]/td[5]/pr-gear-button/div/ul/li[1]/a").get_attribute("title"):
            tolog("Pass: CHAP-Modify option can not be selected")
            result.append(True)
        else:
            tolog("Fail: CHAP-Modify option can be selected")
            result.append(False)

        if "Not Authorized" in driver.find_element_by_xpath("//tr[2]/td[5]/pr-gear-button/div/ul/li[2]/a").get_attribute("title"):
            tolog("Pass: CHAP-Delete option can not be selected")
            result.append(True)
        else:
            tolog("Fail: CHAP-Delete option can be selected")
            result.append(False)

        # Logged in Device
        driver.find_element_by_xpath("//div/div[1]/div/ul/li[9]/ul/li[5]/a/span/span").click()
        time.sleep(1)

        result.append(testLinkAssertEnabled("//div/pr-button-bar/div/div/div/button[2]", False,
                                            "Pass: Logged in Device-Add to initiator list button is disabled",
                                            "Fail: Logged in Device-Add to initiator list button is enabled"))

        if result.count(True) != len(result):
            tolog('\n<font color="red">Fail: View user permissions is failed on Device_ISCSIManagement page </font>')
            tolog(Fail)
        else:
            tolog('\n<font color="green">Pass</font>')
            tolog(Pass)

        # Clear Up
        clearUpCHAP(c)
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