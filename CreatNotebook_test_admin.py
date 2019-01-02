from HtmlTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, os
import HtmlTestRunner


class TEST_CREATENOTEBOOK_ADMIN(unittest.TestCase):

    def Test_CreateNotebook(self):
        driver = test_admin_login()
        driver.find_element_by_id('createNewNotebookLeftNavButton').click()
        driver.find_element_by_id('notebookName').send_keys('Test_Notebook_QingWang')
        driver.find_element_by_name('notebookDescription').send_keys('Test Script execution-01/01/2019')
        driver.find_element_by_name('createNotebook').click()

        test_value = driver.find_element_by_id('NotebookTitle').text
        print(test_value)
        a = 'Test_Notebook_QingWang'
        test_value2 = driver.find_element_by_id('notebookOwnerSpan').text
        b = 'System Administrator'
        test_value3 =driver.find_element_by_id('notebookDescription').text
        print(test_value2)
        c = 'Test Script execution-01/01/2019'

        if a in test_value and b in test_value2 and c in test_value3:
            valid = True
        else:
            valid = False
            picture_name = 'test_CreateNotebookAdmin_' + str(time.strftime('%Y%m%d%H%M%S')) + ' .png'
            driver.get_screenshot_as_file(picture_name)
        self.assertTrue(valid)


def TestAdminlogin():
    driver = webdriver.Chrome('C:\\Users\\QingW\\PycharmProjects\\FirstSeleium\\Driver\\chromedriver.exe')
    driver.get('https://model.arxspan.com/login.asp')
    driver.maximize_window()
    driver.find_element_by_id('login-email').send_keys('admin@demo.com')
    driver.find_element_by_id('login-pass').send_keys('carbonCopee')
    driver.find_element_by_id('login-submit').send_keys(Keys.RETURN)
    time.sleep(1)
    select = Select(driver.find_element_by_tag_name('select'))
    select.select_by_visible_text('Demo')
    driver.find_element_by_id('login-submit').send_keys(Keys.ENTER)
    return driver


listaa = 'C:\\Users\\QingW\\PycharmProjects\\FirstSeleium\\ArxspanAutomationTest\\notebook_test'


def createsuite1():
    testunit=unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(listaa, pattern='CreatNotebook_test_admin.py', top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print(testunit)
    return testunit


if __name__ == '__main__':
    currenttime = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime(time.time()))
    reportfile = 'ResultReport' + currenttime + '.html'
    filename = 'C:\\Users\\QingW\\PycharmProjects\\FirstSeleium\\reports\\result.html'
    fp = open(filename, 'wb')
    filepath = 'C:\\Users\\QingW\\PycharmProjects\\FirstSeleium\\reports'

    runner = HTMLTestRunner(output=filepath)

    runner.run(createsuite1())

    fp.close()

