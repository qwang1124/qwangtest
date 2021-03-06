# Test ID: testELN-01
# Test name: Create the new note book and share to Joe and Jane Test
# Expect output:
#      1. Create a new note book on today's date;
#      2. Add the description as 'Test Script execution-01/01/2019' ;
#      3. Share to Joe as the "read and write";
#      4. Share to Jane as the "read and write";
# Step description:
#      1. Open the Chrome driver;
#      2. Login Admin as the user;
#      3. Create a new note book;
#      4. Add the note book name and description;
#      5. Share the note book to Joe as "read and write";
#      6. Share the note book to Jane as "read and write";
#      7. Verify the sharing notification is displayed
#      8. Log out.
import time, re, os
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import platform
import allure


class TestCreatenotebookAdmin(unittest.TestCase):

    @allure.testcase('test_create_notebook_by_admin')
    def test_create_notebook_by_admin(self):
        # driver = webdriver.Ie()
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get('https://model.arxspan.com/login.asp')
        driver.find_element_by_id('login-email').send_keys('admin@demo.com')
        driver.find_element_by_id('login-pass').send_keys('arxspanLukGood')
        driver.find_element_by_id('login-submit').send_keys(Keys.RETURN)
        time.sleep(1)
        select = Select(driver.find_element_by_tag_name('select'))
        select.select_by_visible_text('Model Test Script Company')
        driver.find_element_by_id('login-submit').send_keys(Keys.ENTER)
        driver.implicitly_wait(10)

        # create notebook by admin
        driver.find_element_by_id('createNewNotebookLeftNavButton').click()
        driver.find_element_by_id('notebookName').send_keys('Test_Note_book_QW')
        driver.find_element_by_name('notebookDescription').send_keys('Test Script execution-01/01/2019')
        driver.find_element_by_name('createNotebook').click()

        test_value = driver.find_element_by_id('NotebookTitle').text
        print(test_value)
        a = 'Test_Note_book_QW'
        test_value2 = driver.find_element_by_id('notebookOwnerSpan').text
        b = 'System Administrator'
        test_value3 = driver.find_element_by_id('notebookDescription').text
        print(test_value2)
        c = 'Test Script execution-01/01/2019'

        if a in test_value and b in test_value2 and c in test_value3:
            valid = True
        else:
            valid = False
            picture_name = 'testcreateNotebookAdmin_' + str(time.strftime('%Y%m%d%H%M%S')) + ' .png'
            driver.get_screenshot_as_file(picture_name)
        self.assertTrue(valid)

        # Share notebook with Joe Chemistry
        driver.find_element_by_id('shareNotebookLink').click()

        driver.find_element_by_class_name('groupSelectLink').click()
        driver.find_element_by_id('groupListUsers-0').click()
        driver.find_element_by_id('listGroupCheckUser-1786').click()
        driver.find_element_by_xpath('//*[@id="groupsDiv"]/div[3]/input').click()
        driver.find_element_by_id('canRead').click()
        driver.find_element_by_id('canWrite').click()
        driver.find_element_by_xpath('//*[@id="shareForm"]/input[8]').click()
        time.sleep(1)

        assert driver.find_element_by_class_name('userName').is_displayed()
        assert driver.find_element_by_class_name('userTitle').is_displayed()
        assert driver.find_elements_by_id('newPermissions')[0].is_displayed()
        # Share test_notebook with Jane Biologist
        time.sleep(1)
        driver.find_element_by_id('shareNotebookLink').click()
        driver.find_element_by_class_name('groupSelectLink').click()
        driver.find_element_by_id('groupListUsers-0').click()
        driver.find_element_by_id('listGroupCheckUser-1787').click()
        driver.find_element_by_xpath('//*[@id="groupsDiv"]/div[3]/input').click()

        driver.find_element_by_id('canRead').click()
        driver.find_element_by_id('canWrite').click()
        driver.find_element_by_xpath('//*[@id="shareForm"]/input[8]').click()
        time.sleep(1)
        # assert driver.find_elements_by_class_name('userName')[1].is_displayed()
        # assert driver.find_element_by_class_name('userTitle').is_displayed()
        # assert driver.find_elements_by_id('newPermissions')[0].is_displayed()

        driver.get('https://model.arxspan.com/arxlab/dashboard.asp')
        time.sleep(2)
        # Verify the Notification of sharing note book is displayed
        assert driver.find_element_by_id('notificationsHolder').is_displayed()

        # Logout
        driver.find_element_by_link_text('Logout').click()
        driver.close()






