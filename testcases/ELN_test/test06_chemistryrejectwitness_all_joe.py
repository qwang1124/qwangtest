# Test ID: testELN-07
# Test name: Joe witnessing rejected biology_concept_experiments and send request to Jane agagin Test
# Expect output:
#      1. Witnessing successful;
#      2. Add new note to the biology_concept_experiments;
#      3. Send the request to Jane again;
# Step description:
#      1. Open the Chrome driver;
#      2. Login Joe as the user;
#      3. Choose 'Model Test Script Company' as the company ;
#      4. Select the biology_concept_experiments and select the notes table;
#      5. Verify the rejection is showing;
#      6. Add a new note to the biology_concept_experiments;
#      7. Sign & Close, selecting Jane Biologist as the Witness;
#      8. Log out.
import time
import unittest


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import allure


class TestWitnessJoe(unittest.TestCase):

    @allure.testcase('witnessjoe')
    def test1(self):
        driver = joelogin()
        driver.implicitly_wait(30)
        WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_css_selector('#navMyExperiments > ul > '
                                                                                           'li:nth-child(1) > '
                                                                                           'a')).click()

        # check the rejection reason is showing
        element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id('noteTable_tab'))
        driver.execute_script("arguments[0].click();", element)
        time.sleep(2)
        driver.find_element_by_link_text('Witness Request Rejection').click()
        # assert driver.find_element_by_class_name('attachmentsIndexTable').is_displayed()

        # add new note
        driver.find_element_by_id('addNoteButton').click()

        text = driver.find_elements_by_css_selector('[class="cke_contents cke_reset"]')[5]
        driver.execute_script("arguments[0].innerHTML = 'TESTING TESTING'", text)
        button = driver.find_element_by_css_selector('#submitRow > a:nth-child(1)')
        button.send_keys(Keys.ENTER)

        # Sign & Close, selecting Jane Biologist as the Witness
        sign = WebDriverWait(driver, 6).until(ec.visibility_of_element_located((By.ID, "signExperimentButton")))
        driver.execute_script("arguments[0].click();", sign)
        email = driver.find_elements_by_id('signEmail')[0]
        email.send_keys('joe@demo.com')
        password = driver.find_elements_by_id('password')[0]
        password.send_keys('carbonCopee')
        checkbox = driver.find_element_by_css_selector('#signDiv > form > section.bottomDisclaimer > div > label')
        checkbox.click()
        select = Select(driver.find_element_by_id('requesteeIdBox'))
        select.select_by_visible_text('Jane Biologist')
        driver.find_element_by_css_selector('#signDivButtons > button:nth-child(1)').click()
        time.sleep(4)

        # logout
        driver.get('https://model.arxspan.com/arxlab/dashboard.asp')
        driver.find_element_by_link_text('Logout').click()
        driver.close()


def joelogin():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://model.arxspan.com/login.asp')
    driver.find_element_by_id('login-email').send_keys('joe@demo.com')
    driver.find_element_by_id('login-pass').send_keys('carbonCopee')
    driver.find_element_by_id('login-submit').send_keys(Keys.RETURN)
    time.sleep(1)
    select = Select(driver.find_element_by_tag_name('select'))
    select.select_by_visible_text('Model Test Script Company')
    driver.find_element_by_id('login-submit').send_keys(Keys.ENTER)
    return driver

