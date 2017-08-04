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

class verify_view_user_permissions_Device_NetworkManagement_page(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://10.84.2.164/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_verify_view_user_permissions_Device_NetworkManagement_page(self):
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
        createISCSIPortal(c)
        time.sleep(3)

        # verify Device page permissions
        driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/ul/li[6]/a/span").click()
        time.sleep(3)

        # Network Management
        tolog("Network Management")
        driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div/div[1]/div/ul/li[7]/a/span/span").click()
        time.sleep(1)
        for i in range(60):
            try:
                if self.is_element_present(By.XPATH, "/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div/div[1]/div/ul/li[7]/ul/li[4]/a/span/span"):
                    driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div/div[1]/div/ul/li[7]/ul/li[1]/a/span/span").click()
                    break
            except: pass
            time.sleep(1)
        else:
            driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div/div[1]/div/ul/li[7]/a/span/span").click()

        time.sleep(1)
        driver.find_element_by_xpath("//tr[2]/td[7]/pr-gear-button/div/a/i").click()

        # Virtual Management Ports IPv4
        tolog("Virtual management Ports IPv4")
        if "Not Authorized" not in driver.find_element_by_xpath("//pr-gear-button/div/ul/li[1]/a").get_attribute("title"):
            tolog("Pass: Virtual management Ports IPv4-View Detail option can be selected")
            result.append(True)
        else:
            tolog("Fail: Virtual management Ports IPv4-View Detail option can not be selected")
            result.append(False)

        if "Not Authorized" in driver.find_element_by_xpath("//pr-gear-button/div/ul/li[2]/a").get_attribute("title"):
            tolog("Pass: Virtual management Ports IPv4-Modify option can not be selected")
            result.append(True)
        else:
            tolog("Fail: Virtual management Ports IPv4-Modify option can be selected")
            result.append(False)

        if "Not Authorized" in driver.find_element_by_xpath("//pr-gear-button/div/ul/li[4]/a").get_attribute("title"):
            tolog("Pass: Virtual management Ports IPv4-Disable option can not be selected")
            result.append(True)
        else:
            tolog("Fail: Virtual management Ports IPv4-Disable option can be selected")
            result.append(False)

        tolog("Virtual management Ports IPv6")
        driver.find_element_by_xpath("//div[2]/div/div/h4").click()
        driver.find_element_by_xpath("//tr[3]/td[7]/pr-gear-button/div/a/i").click()
        time.sleep(3)
        if "Not Authorized" not in driver.find_element_by_xpath("//pr-gear-button/div/ul/li[1]/a").get_attribute("title"):
            tolog("Pass: Virtual management Ports IPv6-View Detail option can be selected")
            result.append(True)
        else:
            tolog("Fail: Virtual management Ports IPv6-View Detail option can not be selected")
            result.append(False)

        if "Not Authorized" in driver.find_element_by_xpath("//pr-gear-button/div/ul/li[2]/a").get_attribute("title"):
            tolog("Pass: Virtual management Ports IPv6-Modify option can not be selected")
            result.append(True)
        else:
            tolog("Fail: Virtual management Ports IPv6-Modify option can be selected")
            result.append(False)

        if "Not Authorized" in driver.find_element_by_xpath("//pr-gear-button/div/ul/li[4]/a").get_attribute("title"):
            tolog("Pass: Virtual management Ports IPv6-Disable option can not be selected")
            result.append(True)
        else:
            tolog("Fail: Virtual management Ports IPv6-Disable option can be selected")
            result.append(False)

        # Physical Management Ports
        tolog("Physical Management Ports IPv4")
        driver.find_element_by_xpath("//tr[2]/td[6]/pr-gear-button/div/a/i").click()
        time.sleep(3)

        if "Not Authorized" not in driver.find_element_by_xpath("//pr-gear-button/div/ul/li[1]/a").get_attribute("title"):
            tolog("Pass: Physical Management Ports IPv4-View Detail option can be selected")
            result.append(True)
        else:
            tolog("Fail: Physical Management Ports IPv4-View Detail option can not be selected")
            result.append(False)

        if "Not Authorized" in driver.find_element_by_xpath("//pr-gear-button/div/ul/li[2]/a").get_attribute("title"):
            tolog("Pass: Physical Management Ports IPv4-Modify option can not be selected")
            result.append(True)
        else:
            tolog("Fail: Physical Management Ports IPv4-Modify option can be selected")
            result.append(False)

        if "Not Authorized" in driver.find_element_by_xpath("//pr-gear-button/div/ul/li[4]/a").get_attribute("title"):
            tolog("Pass: Physical Management Ports IPv4-Disable option can not be selected")
            result.append(True)
        else:
            tolog("Fail: Physical Management Ports IPv4-Disable option can be selected")
            result.append(False)

        tolog("Physical Management Ports IPv6")
        driver.find_element_by_xpath("//div[3]/div/div/h4").click()
        time.sleep(1)
        driver.find_element_by_xpath("//tr[3]/td[6]/pr-gear-button/div/a/i").click()
        time.sleep(3)

        if "Not Authorized" not in driver.find_element_by_xpath("//pr-gear-button/div/ul/li[1]/a").get_attribute(
                "title"):
            tolog("Pass: Physical Management Ports IPv6-View Detail option can be selected")
            result.append(True)
        else:
            tolog("Fail: Physical Management Ports IPv6-View Detail option can not be selected")
            result.append(False)

        if "Not Authorized" in driver.find_element_by_xpath("//pr-gear-button/div/ul/li[2]/a").get_attribute("title"):
            tolog("Pass: Physical Management Ports IPv6-Modify option can not be selected")
            result.append(True)
        else:
            tolog("Fail: Physical Management Ports IPv6-Modify option can be selected")
            result.append(False)

        if "Not Authorized" in driver.find_element_by_xpath("//pr-gear-button/div/ul/li[4]/a").get_attribute("title"):
            tolog("Pass: Physical Management Ports IPv6-Disable option can not be selected")
            result.append(True)
        else:
            tolog("Fail: Physical Management Ports IPv6-Disable option can be selected")
            result.append(False)

        # IO Port
        tolog("IO Port 1")
        for i in range(60):
            try:
                if self.is_element_present(By.XPATH,"/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div/div[1]/div/ul/li[7]/ul/li[4]/a/span/span"):
                    driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div/div[1]/div/ul/li[7]/ul/li[2]/a/span/span").click()
                    break
            except:
                pass
            time.sleep(1)
        else:
            driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div/div[1]/div/ul/li[7]/a/span/span").click()

        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[2]/div/div/div[2]/div/div/table[2]/tbody/tr[2]/td[1]/input").click()
        time.sleep(3)

        result.append(testLinkAssertEnabled("//pr-button-bar/div/div/div/button[1]", True,
                                            "Pass: Port-View button is enabled",
                                            "Fail: Port-View button is disabled"))
        result.append(testLinkAssertEnabled("//pr-button-bar/div/div/div/button[2]", False,
                                            "Pass: Port-Modify button is disabled",
                                            "Fail: Port-Modify button is enabled"))
        result.append(testLinkAssertEnabled("//pr-button-bar/div/div/div/button[3]", False,
                                            "Pass: Port-Ping button is disabled",
                                            "Fail: Port-Ping button is enabled"))

        driver.find_element_by_xpath("//tr[2]/td[10]/pr-gear-button/div/a/i").click()
        time.sleep(3)

        if "Not Authorized" not in driver.find_element_by_xpath("//tr[2]/td[10]/pr-gear-button/div/ul/li[1]/a").get_attribute("title"):
            tolog("Pass: Port1-View Detail option can be selected")
            result.append(True)
        else:
            tolog("Fail: Port1-View Detail option can not be selected")
            result.append(False)

        if "Not Authorized" in driver.find_element_by_xpath("//tr[2]/td[10]/pr-gear-button/div/ul/li[2]/a").get_attribute("title"):
            tolog("Pass: Port1-Modify option can not be selected")
            result.append(True)
        else:
            tolog("Fail: Port1-Modify option can be selected")
            result.append(False)

        if "Not Authorized" in driver.find_element_by_xpath("//tr[2]/td[10]/pr-gear-button/div/ul/li[3]/a").get_attribute("title"):
            tolog("Pass: Port1-Ping option can not be selected")
            result.append(True)
        else:
            tolog("Fail: Port1-Ping option can be selected")
            result.append(False)

        tolog("IO Port 2")
        driver.find_element_by_xpath("//pr-page-header/div/div/div[1]/h3").click()
        time.sleep(1)
        driver.find_element_by_xpath("//tr[3]/td[10]/pr-gear-button/div/a/i").click()
        time.sleep(3)

        if "Not Authorized" not in driver.find_element_by_xpath("//tr[2]/td[10]/pr-gear-button/div/ul/li[1]/a").get_attribute("title"):
            tolog("Pass: Port2-View Detail option can be selected")
            result.append(True)
        else:
            tolog("Fail: Port2-View Detail option can not be selected")
            result.append(False)

        if "Not Authorized" in driver.find_element_by_xpath("//tr[2]/td[10]/pr-gear-button/div/ul/li[2]/a").get_attribute("title"):
            tolog("Pass: Port2-Modify option can not be selected")
            result.append(True)
        else:
            tolog("Fail: Port2-Modify option can be selected")
            result.append(False)

        if "Not Authorized" in driver.find_element_by_xpath("//tr[2]/td[10]/pr-gear-button/div/ul/li[3]/a").get_attribute("title"):
            tolog("Pass: Port2-Ping option can not be selected")
            result.append(True)
        else:
            tolog("Fail: Port2-Ping option can be selected")
            result.append(False)

        # Portal
        tolog("Portal")
        for i in range(60):
            try:
                if self.is_element_present(By.XPATH,"/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div/div[1]/div/ul/li[7]/ul/li[4]/a/span/span"):
                    driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div/div[1]/div/ul/li[7]/ul/li[3]/a/span/span").click()
                    break
            except:
                pass
            time.sleep(1)
        else:
            driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div/div[1]/div/ul/li[7]/a/span/span").click()

        time.sleep(1)
        driver.find_element_by_xpath("//table[2]/tbody/tr[2]/td[1]/input").click()
        time.sleep(3)

        result.append(testLinkAssertEnabled("//pr-button-bar/div/div/div/button[1]", True,
                                            "Pass: Portal-View button is enabled",
                                            "Fail: Portal-View button is disabled"))
        result.append(testLinkAssertEnabled("//pr-button-bar/div/div/div/button[2]", False,
                                            "Pass: Portal-Modify button is disabled",
                                            "Fail: Portal-Modify button is enabled"))
        result.append(testLinkAssertEnabled("//pr-button-bar/div/div/div/button[3]", False,
                                            "Pass: Portal-Delete button is disabled",
                                            "Fail: Portal-Delete button is enabled"))
        result.append(testLinkAssertEnabled("//pr-button-bar/div/div/div/button[4]", False,
                                            "Pass: Portal-Add Portal Button is disabled",
                                            "Fail: Portal-Add Portal Button is enabled"))

        driver.find_element_by_xpath("//tr[2]/td[10]/pr-gear-button/div/a/i").click()
        time.sleep(3)

        if "Not Authorized" not in driver.find_element_by_xpath("//tr[2]/td[10]/pr-gear-button/div/ul/li[1]/a").get_attribute("title"):
            tolog("Pass: Portal-View Detail option can be selected")
            result.append(True)
        else:
            tolog("Fail: Portal-View Detail option can not be selected")
            result.append(False)

        if "Not Authorized" in driver.find_element_by_xpath("//tr[2]/td[10]/pr-gear-button/div/ul/li[2]/a").get_attribute("title"):
            tolog("Pass: Portal-Modify option can not be selected")
            result.append(True)
        else:
            tolog("Fail: Portal-Modify option can be selected")
            result.append(False)

        if "Not Authorized" in driver.find_element_by_xpath("//tr[2]/td[10]/pr-gear-button/div/ul/li[3]/a").get_attribute("title"):
            tolog("Pass: Portal-Delete option can not be selected")
            result.append(True)
        else:
            tolog("Fail: Portal-Delete option can be selected")
            result.append(False)

        # Trunk
        tolog("Trunk")
        # create trunk
        createTrunk(c)
        time.sleep(3)
        for i in range(60):
            try:
                if self.is_element_present(By.XPATH,"/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div/div[1]/div/ul/li[7]/ul/li[4]/a/span/span"):
                    driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div/div[1]/div/ul/li[7]/ul/li[4]/a/span/span").click()
                    break
            except:
                pass
            time.sleep(1)
        else:
            driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div/div[1]/div/ul/li[7]/a/span/span").click()

        time.sleep(1)
        driver.find_element_by_xpath("//div/div[2]/table[2]/tbody/tr[2]/td[1]/input").click()
        time.sleep(3)

        result.append(testLinkAssertEnabled("//pr-button-bar/div/div/div/button[1]", False,
                                            "Pass: Trunk-Modify button is disabled",
                                            "Fail: Trunk-Modify button is enabled"))
        result.append(testLinkAssertEnabled("//pr-button-bar/div/div/div/button[2]", False,
                                            "Pass: Trunk-Delete button is disabled",
                                            "Fail: Trunk-Delete button is enabled"))
        result.append(testLinkAssertEnabled("//pr-button-bar/div/div/div/button[3]", False,
                                            "Pass: Trunk-Add Trunk Button is disabled",
                                            "Fail: Trunk-Add Trunk Button is enabled"))

        driver.find_element_by_xpath("//tr[2]/td[9]/pr-gear-button/div/a/i").click()
        time.sleep(3)

        if "Not Authorized" in driver.find_element_by_xpath("//tr[2]/td[9]/pr-gear-button/div/ul/li[1]/a").get_attribute("title"):
            tolog("Pass: Trunk-Modify option can not be selected")
            result.append(True)
        else:
            tolog("Fail: Trunk-Modify option can be selected")
            result.append(False)

        if "Not Authorized" in driver.find_element_by_xpath("//tr[2]/td[9]/pr-gear-button/div/ul/li[2]/a").get_attribute("title"):
            tolog("Pass: Trunk-Delete option can not be selected")
            result.append(True)
        else:
            tolog("Fail: Trunk-Delete option can be selected")
            result.append(False)

        if result.count(True) != len(result):
            tolog('\n<font color="red">Fail: View user permissions is failed on Device_NetworkManagement page </font>')
            tolog(Fail)
        else:
            tolog('\n<font color="green">Pass</font>')
            tolog(Pass)

        # Clear Up
        clearUpTrunk(c)
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
