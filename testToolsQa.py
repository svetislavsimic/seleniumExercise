import unittest
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
import datetime
class ToolsQa(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()


    def test_search_in_tools_qa(self):
        driver = self.driver
        driver.get('http://www.toolsqa.com/automation-practice-form/')
        s1 = Select(driver.find_element_by_id('continents'))


        for opt in s1.options:
            print(opt.text)
            s1.select_by_visible_text(opt.text)
<<<<<<< HEAD
            time.sleep(1.5)

=======
            time.sleep(0.5)
>>>>>>> c63b5cd6fd297ce5eafbd70ca8a1f6798443507c

    def test_my_info(self):
        driver = self.driver
        driver.get('https://www.toolsqa.com/automation-practice-form/')
        fnentry = driver.find_element_by_xpath("//input[@name='firstname']")
        fnentry.click()
        fnentry.clear()
        fnentry.send_keys("Petar")
        lnentry = driver.find_element_by_xpath("//input[@name='lastname']")
        lnentry.click()
        lnentry.clear()
        lnentry.send_keys("Tasovac")
        genderbutton = driver.find_element_by_xpath("//input[@value='Male']")
        genderbutton.click()
        yoebutton = driver.find_element_by_xpath("//input[@id='exp-0']")
        yoebutton.click()
        datepicker = driver.find_element_by_xpath("//input[@id='datepicker']")
        datepicker.click()
        datepicker.clear()
        a = datetime.datetime.now()
        datepicker.send_keys(a.strftime('%d.%m.%Y'))
        professioncheck1 = driver.find_element_by_xpath("//input[@value='Manual Tester']")
        professioncheck2 = driver.find_element_by_xpath("//input[contains(@value,'Automation Tester')]")
        professioncheck1.click()
        professioncheck2.click()
        toolselect = driver.find_element_by_xpath("//input[@id='tool-2']")
        toolselect.click()
        s1 = Select(driver.find_element_by_id('continents'))
        s1.select_by_visible_text("Europe")
        selcommands = driver.find_element_by_xpath("//option[contains(.,'Browser Commands')]")
        selcommands.click()
        time.sleep(15)
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()