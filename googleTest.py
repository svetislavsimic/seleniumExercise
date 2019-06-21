import unittest
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC

class FacebookTesting(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()


    def testGoogleSearch(self):
        driver = self.driver
        driver.get('https://www.google.com')
        luckybtn = driver.find_element_by_xpath("(//input[contains(@type,'submit')])[4]")
        luckybtn.click()
        ribbon = driver.find_element_by_xpath("(//div[contains(@class,'ribbon')])[1]")
        ribbontext = ribbon.text
        print(ribbontext)
        time.sleep(2)
        assert "Jun 22" in ribbontext
    def tearDown(self):
        self.driver.close()
