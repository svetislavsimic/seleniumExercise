import unittest
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
class FacebookTesting(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()


    def testGoogleSearch(self):
        driver = self.driver
        driver.get('https://www.blic.rs/')
        politika = driver.find_element_by_xpath("//a[@href='/vesti/politika']")
        # politika.send_keys(Keys.CONTROL, Keys.RETURN)
        # time.sleep(3)
        #https://www.blic.rs/vesti/politika
        politikahref = politika.get_attribute("href")
        print(politikahref)
        driver.execute_script("window.open('{}')".format(politikahref))

        window2 = driver.window_handles[1]

        driver.switch_to.window(window2)
    def tearDown(self):
        self.driver.close()
