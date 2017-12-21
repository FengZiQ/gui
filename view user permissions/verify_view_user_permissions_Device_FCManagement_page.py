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

class verify_view_user_permissions_Device_FCManagement_page(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://10.84.2.164/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_verify_view_user_permissions_Device_FCManagement_page(self):
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

        # verify Device page permissions
        driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/ul/li[6]/a/span").click()
        time.sleep(3)

        # FC Management
        tolog("FC Management")
        driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div/div[1]/div/ul/li[8]/a/i").click()
        time.sleep(1)
        # Node
        for i in range(60):
            try:
                if self.is_element_present(By.XPATH,"/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div/div[1]/div/ul/li[8]/ul/li[6]/a/span/span"):
                    driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div/div[1]/div/ul/li[8]/ul/li[1]/a/span/span").click()
                    time.sleep(1)
                    break
            except:
                pass
            time.sleep(1)
        else:
            driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div/div[1]/div/ul/li[8]/a/i").click()

        if 'FC Node Information' in driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[2]/div/div/div[2]/div/div/h4").text:
            tolog("Pass: Node list can be opened")
            result.append(True)
        else:
            tolog("Fail: Node list can not be opened")

        # Port
        tolog("port")

        for i in range(60):
            try:
                if self.is_element_present(By.XPATH,"/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div/div[1]/div/ul/li[8]/ul/li[6]/a/span/span"):
                    driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div/div[1]/div/ul/li[8]/ul/li[2]/a/span/span").click()
                    break
            except:
                pass
            time.sleep(1)
        else:
            driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div/div[1]/div/ul/li[8]/a/i").click()

        time.sleep(1)
        driver.find_element_by_xpath("//div/div[2]/table[2]/tbody/tr[2]/td[1]/input").click()
        time.sleep(3)

        result.append(testLinkAssertEnabled("//pr-button-bar/div/div/div/button[1]", True,
                                            "Pass: FCPort-View button is enabled",
                                            "Fail: FCPort-View button is disabled"))
        result.append(testLinkAssertEnabled("//pr-button-bar/div/div/div/button[2]", False,
                                            "Pass: FCPort-Modify button is disabled",
                                            "Fail: FCPort-Modify button is enabled"))
        result.append(testLinkAssertEnabled("//pr-button-bar/div/div/div/button[3]", False,
                                            "Pass: FCPort-Reset Button is disabled",
                                            "Fail: FCPort-Reset Button is enabled"))
        result.append(testLinkAssertEnabled("//pr-button-bar/div/div/div/button[4]", False,
                                            "Pass: FCPort-Ping Button is disabled",
                                            "Fail: FCPort-Ping Button is enabled"))

        driver.find_element_by_xpath("//tr[2]/td[9]/pr-gear-button/div/a/i").click()
        time.sleep(3)

        if "Not Authorized" not in driver.find_element_by_xpath("//tr[2]/td[9]/pr-gear-button/div/ul/li[1]/a").get_attribute("title"):
            tolog("Pass: FCPort-View option can be selected")
            result.append(True)
        else:
            tolog("Fail: FCPort-View option can not be selected")
            result.append(False)

        if "Not Authorized" in driver.find_element_by_xpath("//tr[2]/td[9]/pr-gear-button/div/ul/li[2]/a").get_attribute("title"):
            tolog("Pass: FCPort-Modify option can not be selected")
            result.append(True)
        else:
            tolog("Fail: FCPort-Modify option can be selected")
            result.append(False)

        if "Not Authorized" in driver.find_element_by_xpath("//tr[2]/td[9]/pr-gear-button/div/ul/li[3]/a").get_attribute("title"):
            tolog("Pass: FCPort-Reset option can not be selected")
            result.append(True)
        else:
            tolog("Fail: FCPort-Reset option can be selected")
            result.append(False)

        if "Not Authorized" in driver.find_element_by_xpath("//tr[2]/td[9]/pr-gear-button/div/ul/li[4]/a").get_attribute("title"):
            tolog("Pass: FCPort-Ping option can not be selected")
            result.append(True)
        else:
            tolog("Fail: FCPort-Ping option can be selected")
            result.append(False)

        # Statistics
        tolog("Statistics")
        for i in range(60):
            try:
                if self.is_element_present(By.XPATH,"/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div/div[1]/div/ul/li[8]/ul/li[6]/a/span/span"):
                    driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div/div[1]/div/ul/li[8]/ul/li[3]/a/span/span").click()
                    break
            except:
                pass
            time.sleep(1)
        else:
            driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div/div[1]/div/ul/li[8]/a/i").click()

        time.sleep(1)
        driver.find_element_by_xpath("//tr[2]/td[1]/input").click()
        time.sleep(3)

        result.append(testLinkAssertEnabled("//pr-button-bar/div/div/div/button[1]", True,
                                            "Pass: Statistics-View button is enabled",
                                            "Fail: Statistics-View button is disabled"))
        result.append(testLinkAssertEnabled("//pr-button-bar/div/div/div/button[2]", False,
                                            "Pass: Statistics-Clear button is disabled",
                                            "Fail: Statistics-Clear button is enabled"))

        driver.find_element_by_xpath("//tr[2]/td[6]/pr-gear-button/div/a/i").click()
        time.sleep(3)

        if "Not Authorized" not in driver.find_element_by_xpath("//tr[2]/td[6]/pr-gear-button/div/ul/li[1]/a").get_attribute("title"):
            tolog("Pass: Statistics-View option can be selected")
            result.append(True)
        else:
            tolog("Fail: Statistics-View option can not be selected")
            result.append(False)

        if "Not Authorized" in driver.find_element_by_xpath("//tr[2]/td[6]/pr-gear-button/div/ul/li[2]/a").get_attribute("title"):
            tolog("Pass: Statistics-Clear option can not be selected")
            result.append(True)
        else:
            tolog("Fail: Statistics-Clear option can be selected")
            result.append(False)

        # Logged In Device
        tolog("Logged In Device")
        for i in range(60):
            try:
                if self.is_element_present(By.XPATH,"/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div/div[1]/div/ul/li[8]/ul/li[6]/a/span/span"):
                    driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div/div[1]/div/ul/li[8]/ul/li[4]/a/span/span").click()
                    break
            except:
                pass
            time.sleep(1)
        else:
            driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div/div[1]/div/ul/li[8]/a/i").click()

        time.sleep(1)

        result.append(testLinkAssertEnabled("//pr-button-bar/div/div/div/button[2]", False,
                                            "Pass: Logged In Device-Add to Initiator List button is disabled",
                                            "Fail: Logged In Device-Add to Initiator List button is enabled"))

        # Device on Fabric
        tolog("Device on Fabric")
        for i in range(60):
            try:
                if self.is_element_present(By.XPATH,"/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div/div[1]/div/ul/li[8]/ul/li[6]/a/span/span"):
                    driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div/div[1]/div/ul/li[8]/ul/li[5]/a/span/span").click()
                    break
            except:
                pass
            time.sleep(1)
        else:
            driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div/div[1]/div/ul/li[8]/a/i").click()

        time.sleep(1)

        result.append(testLinkAssertEnabled("//pr-button-bar/div/div/div/button", False,
                                            "Pass: Device on Fabric-Add to Initiator List button is disabled",
                                            "Fail: Device on Fabric-Add to Initiator List button is enabled"))

        # SFP
        tolog("SFP")
        for i in range(60):
            try:
                if self.is_element_present(By.XPATH,"/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div/div[1]/div/ul/li[8]/ul/li[6]/a/span/span"):
                    driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div/div[1]/div/ul/li[8]/ul/li[6]/a/span/span").click()
                    break
            except:
                pass
            time.sleep(1)
        else:
            driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div/div[1]/div/ul/li[8]/a/i").click()

        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[2]/div/div/div[2]/div/div/table[2]/tbody/tr[2]/td[1]").click()
        time.sleep(1)

        result.append(testLinkAssertEnabled("//pr-button-bar/div/div/div/button", True,
                                            "Pass: SFP-View button is enabled",
                                            "Fail: SFP-View button is disabled"))


        if result.count(True) != len(result):
            tolog('\n<font color="red">Fail: View user permissions is failed on Device_FCManagement page </font>')
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
