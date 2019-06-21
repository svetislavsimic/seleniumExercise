import unittest
from selenium import webdriver
from selenium.webdriver.support.select import Select
import datetime


class ToolsQa(unittest.TestCase):

    date_now = datetime.datetime.now()

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_tools_qa(self):
        driver = self.driver
        driver.implicitly_wait(10)
        driver.get('http://www.toolsqa.com/automation-practice-form/')

        firstname = driver.find_element_by_xpath("//input[@name='firstname']")
        firstname.clear()
        firstname.send_keys('Marko')

        lastname = driver.find_element_by_xpath("//input[@name='lastname']")
        lastname.clear()
        lastname.send_keys('Fuček')

        '''sex male'''
        driver.find_element_by_xpath("//input[contains(@id,'sex-0')]").click()

        '''years of experience'''
        driver.find_element_by_xpath("//input[contains(@id,'exp-0')]").click()

        '''date input field'''
        date_field = driver.find_element_by_xpath("//input[contains(@id,'datepicker')]")
        date_field.clear()
        date_field.send_keys(self.date_now.strftime("%d.%m.%Y"))

        '''Profession'''
        driver.find_element_by_xpath("//input[contains(@id,'profession-1')]").click()

        '''Automation Tool'''
        driver.find_element_by_xpath("//input[contains(@id,'tool-2')]").click()

        continents = Select(driver.find_element_by_xpath("//select[contains(@id,'continents')]"))
        continents.select_by_visible_text('Europe')

        '''Selenium Commands'''
        driver.find_element_by_xpath("//option[contains(.,'Wait Commands')]").click()

        '''Button'''
        driver.find_element_by_xpath("//button[contains(@id,'submit')]").click()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()