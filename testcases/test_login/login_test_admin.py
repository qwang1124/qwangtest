#!/usr/bin/python
# -*- coding: utf-8 -*-
# Test ID: test-01
# Test name: Login Test
# Expect output: Login successful
# Step description:
#      1. Open the Chrome driver;
#      2. Input the URL of test_login page;
#      3. Input the test_admin as the username;
#      4. Input the password;
#      5. Choose the different company;

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import unittest, time, re, os
import allure


class LoginTestAdmin(unittest.TestCase):

    @allure.testcase('test_login test demo')
    def test(self):
        driver = webdriver.Ie()
        driver.get('https://model.arxspan.com/login.asp')
        driver.maximize_window()
        driver.find_element_by_id('login-email').send_keys('admin@demo.com')
        driver.find_element_by_id('login-pass').send_keys('carbonCopee')
        driver.find_element_by_id('login-submit').send_keys(Keys.RETURN)
        select = Select(driver.find_element_by_tag_name('select'))
        select.select_by_visible_text('Model Test Script Company')
        driver.find_element_by_id('login-submit').send_keys(Keys.ENTER)
    # def test1(self):
    #     driver = self.driver
    #     driver.get(self.base_url)
    #     driver.maximize_window()
    #     driver.find_element_by_id('test_login-email').send_keys('admin@demo.com')
    #     driver.find_element_by_id('test_login-pass').send_keys('carbonCopee')
    #     driver.find_element_by_id('test_login-submit').send_keys(Keys.RETURN)
    #     time.sleep(1)
    #     select = Select(driver.find_element_by_tag_name('select'))
    #     select.select_by_visible_text('Demo')
    #     driver.find_element_by_id('test_login-submit').send_keys(Keys.ENTER)
    #     time.sleep(3)
    #     driver.switch_to.window(driver.window_handles[-1])
    #     # driver.switch_to.frame("submitFrame")
    #     test_value = driver.find_element_by_class_name('headUserName').text
    #     a = u'System Administrator'
    #     test_value2 = driver.find_element_by_class_name('companySection').text
    #     b = u'Demo'
    #
    #     if a in test_value and b in test_value2:
    #         valid = True
    #     else:
    #         valid = False
    #         picture_name = 'test_2_' + str(time.strftime('%Y%m%d%H%M%S')) + ' .png'
    #         driver.get_screenshot_as_file(picture_name)
    #     self.assertTrue(valid)

    # @allure.testcase('test_login test bim')
    # def test2(self):
    #     driver = self.driver
    #     driver.get(self.base_url)
    #     driver.maximize_window()
    #     driver.find_element_by_id('test_login-email').send_keys('admin@demo.com')
    #     driver.find_element_by_id('test_login-pass').send_keys('carbonCopee')
    #     driver.find_element_by_id('test_login-submit').send_keys(Keys.RETURN)
    #     time.sleep(1)
    #     select = Select(driver.find_element_by_tag_name('select'))
    #     select.select_by_visible_text('BIM')
    #     driver.find_element_by_id('test_login-submit').send_keys(Keys.ENTER)
    #     time.sleep(3)
    #     driver.switch_to.window(driver.window_handles[-1])
    #     test_value = driver.find_element_by_class_name('headUserName').text
    #     print(test_value)
    #     a = u'System Administrator'
    #     test_value2 = driver.find_element_by_class_name('companySection').text
    #     print(test_value2)
    #     b = u'BIM'
    #
    #     if a in test_value and b in test_value2:
    #         valid = True
    #     else:
    #         valid = False
    #         picture_name = 'test_3_' + str(time.strftime('%Y%m%d%H%M%S')) + ' .png'
    #         driver.get_screenshot_as_file(picture_name)
    #     self.assertTrue(valid)
    #
    # @allure.testcase('test_login test ct demo')
    # def test3(self):
    #     driver = self.driver
    #     driver.get(self.base_url)
    #     driver.maximize_window()
    #     driver.find_element_by_id('test_login-email').send_keys('admin@demo.com')
    #     driver.find_element_by_id('test_login-pass').send_keys('carbonCopee')
    #     driver.find_element_by_id('test_login-submit').send_keys(Keys.RETURN)
    #     time.sleep(1)
    #     select = Select(driver.find_element_by_tag_name('select'))
    #     select.select_by_visible_text('CT DEMO')
    #     driver.find_element_by_id('test_login-submit').send_keys(Keys.ENTER)
    #     time.sleep(3)
    #     driver.switch_to.window(driver.window_handles[-1])
    #     test_value = driver.find_element_by_class_name('headUserName').text
    #     print(test_value)
    #     a = u'System Administrator'
    #     test_value2 = driver.find_element_by_class_name('companySection').text
    #     print(test_value2)
    #     b = u'CT DEMO'
    #
    #     if a in test_value and b in test_value2:
    #         valid = True
    #     else:
    #         valid = False
    #         picture_name = 'test_4_' + str(time.strftime('%Y%m%d%H%M%S')) + ' .png'
    #         driver.get_screenshot_as_file(picture_name)
    #     self.assertTrue(valid)
    #
    # @allure.testcase('test_login test formulation demo')
    # def test4(self):
    #     driver = self.driver
    #     driver.get(self.base_url)
    #     driver.maximize_window()
    #     driver.find_element_by_id('test_login-email').send_keys('admin@demo.com')
    #     driver.find_element_by_id('test_login-pass').send_keys('carbonCopee')
    #     driver.find_element_by_id('test_login-submit').send_keys(Keys.RETURN)
    #     time.sleep(1)
    #     select = Select(driver.find_element_by_tag_name('select'))
    #     select.select_by_visible_text('Formulation Demo')
    #     driver.find_element_by_id('test_login-submit').send_keys(Keys.ENTER)
    #     time.sleep(3)
    #     driver.switch_to.window(driver.window_handles[-1])
    #     test_value = driver.find_element_by_class_name('headUserName').text
    #     print(test_value)
    #     a = u'System Administrator'
    #     test_value2 = driver.find_element_by_class_name('companySection').text
    #     print(test_value2)
    #     b = u'Formulation Demo'
    #
    #     if a in test_value and b in test_value2:
    #         valid = True
    #     else:
    #         valid = False
    #         picture_name = 'test_5_' + str(time.strftime('%Y%m%d%H%M%S')) + ' .png'
    #         driver.get_screenshot_as_file(picture_name)
    #     self.assertTrue(valid)
    #
    # @allure.testcase('test_login test model company')
    # def test5(self):
    #     driver = self.driver
    #     driver.get(self.base_url)
    #     driver.maximize_window()
    #     driver.find_element_by_id('test_login-email').send_keys('admin@demo.com')
    #     driver.find_element_by_id('test_login-pass').send_keys('carbonCopee')
    #     driver.find_element_by_id('test_login-submit').send_keys(Keys.RETURN)
    #     time.sleep(1)
    #     select = Select(driver.find_element_by_tag_name('select'))
    #     select.select_by_visible_text('Model Test Script Company')
    #     driver.find_element_by_id('test_login-submit').send_keys(Keys.ENTER)
    #     time.sleep(3)
    #     driver.switch_to.window(driver.window_handles[-1])
    #     test_value = driver.find_element_by_class_name('headUserName').text
    #     print(test_value)
    #     a = u'System Administrator'
    #     test_value2 = driver.find_element_by_class_name('companySection').text
    #     print(test_value2)
    #     b = u'Model Test Script Company'
    #
    #     if a in test_value and b in test_value2:
    #         valid = True
    #     else:
    #         valid = False
    #         picture_name = 'test_6_' + str(time.strftime('%Y%m%d%H%M%S')) + ' .png'
    #         driver.get_screenshot_as_file(picture_name)
    #     self.assertTrue(valid)
