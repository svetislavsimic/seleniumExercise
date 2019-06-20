import unittest
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time
import datetime


class ToolsQa(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_myData(self):
        driver = self.driver
        driver.get('http://www.toolsqa.com/automation-practice-form/')
        name = driver.find_element_by_xpath("//input[contains(@name,'firstname')]")
        name.clear()
        name.send_keys("Nevena i Gaga")
        time.sleep(3)

        surname = driver.find_element_by_xpath("//input[contains(@name,'lastname')]")
        surname.clear()
        surname.send_keys("M i G")
        time.sleep(3)

        sex = driver.find_element_by_xpath("//input[contains(@id,'sex-1')]").click()
        time.sleep(3)

        expirience = driver.find_element_by_xpath("//input[contains(@id,'exp-6')]").click()
        time.sleep(3)

        vreme = driver.find_element_by_xpath("//input[contains(@id,'datepicker')]")
        datum = datetime.datetime.now()
        vreme.send_keys(datum.strftime('%d.%m.%Y'))
        time.sleep(3)


        profession = driver.find_element_by_xpath("//input[contains(@id,'profession-1')]").click()
        time.sleep(3)

        automatation_Tool = driver.find_element_by_xpath("//input[contains(@id,'tool-2')]").click()
        time.sleep(3)


        Continents  =  Select(driver.find_element_by_id('continents'))

        Continents.select_by_visible_text('Europe')
        time.sleep(3)

        button = driver.find_element_by_xpath("//button[contains(@id,'submit')]").click()



    def tearDown(self):
            self.driver.close()

if __name__ == "__main__":
            unittest.main()