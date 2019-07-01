#Za domaci 11.06. :
#* otvorite stranicu https://www.python.org/
#* kliknite na tab News
#***************************************************************

import unittest
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

class TestClickNews(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()


    def clickonNews(self):
        driver = self.driver
        driver.get("http://www.python.org")
        s1 = Select(driver.find_element_by_name("News from around the Python world"))

        s1.select_by_visible_text('Python News')

        for opt in s1.options:
            print(opt.text)
            s1.select_by_visible_text(opt.text)
            time.sleep(5)


