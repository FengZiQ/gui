# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from to_log import tolog
import unittest, time, re

Pass = "'result': 'p'"
Fail = "'result': 'f'"

class AddDifferentTypesUsers(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://10.84.2.164/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_addDifferentTypesUsers(self):
        FailFlag = False
        driver = self.driver
        driver.get(self.base_url + "/")
        for i in range(60):
            try:
                if self.is_element_present(By.CSS_SELECTOR, "h1.system-name.ng-binding"): break
            except:
                pass
            time.sleep(1)
        else:
            self.fail("time out")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("password")
        time.sleep(0.5)
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("administrator")
        time.sleep(0.5)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        for i in range(60):
            try:
                if self.is_element_present(By.CSS_SELECTOR, "h4.header-title.ng-binding"): break
            except:
                pass
            time.sleep(1)
        else:
            self.fail("time out")

        driver.find_element_by_link_text("User").click()
        userName = ['a', '12', 'a_1', 'testLength123456789012345678901']
        password = ['1', '@', '\\', 'aaaa1aaaa2aaaa3aaaa4aaaa5aaaa6a']
        email = ['1@b.com', '1@a.cn', 'b@b.com.cn', 'c@b.cn.com']
        privilege = ['View', 'Maintenance', 'Power', 'Super']
        for myI in range(0, 4):
            driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
            time.sleep(2)
            driver.find_element_by_name("id").clear()
            driver.find_element_by_name("id").send_keys(userName[myI])
            time.sleep(0.5)
            driver.find_element_by_name("fulllname").clear()
            driver.find_element_by_name("fulllname").send_keys(userName[myI])
            time.sleep(0.5)
            driver.find_element_by_name("password").clear()
            driver.find_element_by_name("password").send_keys(password[myI])
            time.sleep(0.5)
            driver.find_element_by_name("retypepassword").clear()
            driver.find_element_by_name("retypepassword").send_keys(password[myI])
            time.sleep(0.5)
            driver.find_element_by_name("email").clear()
            driver.find_element_by_name("email").send_keys(email[myI])
            time.sleep(0.5)
            Select(driver.find_element_by_name("privilege")).select_by_visible_text(privilege[myI])
            # driver.find_element_by_css_selector("option[value=\"string:Maintenance\"]").click()
            driver.find_element_by_xpath("//button[@type='submit']").click()

            for i in range(60):
                try:
                    if self.is_element_present(By.XPATH, "(//button[@type='button'])[4]"): break
                except: pass
                time.sleep(1)
            else: self.fail("time out")
            self.assertEqual(userName[myI], driver.find_element_by_xpath("//tr[" + str(3 + myI) + "]/td[2]").text)
            self.assertEqual(privilege[myI], driver.find_element_by_xpath("//tr[" + str(3 + myI) + "]/td[4]").text)

            if driver.find_element_by_xpath("//tr[" + str(3 + myI) + "]/td[2]").text != userName[myI]:
                FailFlag = True
                tolog('add ' + userName[myI] + ' user is failed')
            elif driver.find_element_by_xpath("//tr[" + str(3 + myI) + "]/td[4]").text != privilege[myI]:
                FailFlag = True
                tolog('add ' + privilege[myI] + ' user is failed')
            elif driver.find_element_by_xpath("//tr[" + str(3 + myI) + "]/td[2]").text == userName[myI] and driver.find_element_by_xpath("//tr[" + str(3 + myI) + "]/td[4]").text == privilege[myI]:
                tolog('add ' + privilege[myI] + ' ' + userName[myI] + ' user is passed')

        if FailFlag:
            tolog('\n<font color="red">Fail: add user is failed </font>')
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
