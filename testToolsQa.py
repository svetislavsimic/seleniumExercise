import unittest
from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep
import datetime


class ToolsQa(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_form_tools_qa(self):
        a = datetime.datetime.now()
        driver = self.driver
        driver.get('http://www.toolsqa.com/automation-practice-form/')
        #s1 = Select(driver.find_element_by_xpath('continents'))
        element = driver.find_element_by_xpath("//input[@name='firstname']")
        element.clear()
        element.send_keys('Marko')
        element = driver.find_element_by_xpath("//input[@name='lastname']")
        element.clear()
        element.send_keys('Fucek')
        element = driver.find_element_by_xpath("//input[contains(@value,'Male')]").click()
        element = driver.find_element_by_xpath("//input[contains(@value,'1')]").click()
        element = driver.find_element_by_xpath("//input[contains(@id,'datepicker')]").send_keys(a.strftime("%d.%m.%Y"))
        element = driver.find_element_by_xpath("//input[@value='Automation Tester']").click()
        element = driver.find_element_by_xpath("//input[contains(@id,'tool-2')]").click()
        s1 = Select(driver.find_element_by_xpath("//select[contains(@id,'continents')]"))





        #element.Select(driver.find_element_by_xpath("//input[contains(@value,'Male')]")).click()
        #sleep(4)


        s1.select_by_visible_text('Europe')

        # for opt in s1.options:
        #     print(opt.text)
        #     s1.select_by_visible_text(opt.text)
        #     time.sleep(10)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()