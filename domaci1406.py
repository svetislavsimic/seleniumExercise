import unittest
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

class Guru99 (unittest.TestCase):



    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_Country(self):
        driver = self.driver
        driver.get('http://demo.guru99.com/test/newtours/register.php')
        s1 = Select(driver.find_element_by_name("country"))
        s1.select_by_visible_text('BARBADOS')
        time.sleep(10)

    def tearDown(self):
            self.driver.close()

if __name__ == "__main__":
        unittest.main()