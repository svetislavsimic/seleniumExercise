import unittest
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC

class FacebookTesting(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()


    def testWindowSweetching(self):
        driver = self.driver

        driver.get("https://www.instagram.com/")
        driver.maximize_window()
        window_no1 = driver.window_handles[0]

        window_no1_title = driver.title

        driver.execute_script("window.open('http://www.twitter.com')")

        window_no2 = driver.window_handles[1]

        driver.switch_to.window(window_no2)

        window_no2_title = driver.title

        time.sleep(1)

        driver.execute_script("window.open('https://www.blic.rs/')")

        window_no3 = driver.window_handles[2]

        driver.switch_to.window(window_no3)



        assert window_no1_title != window_no2_title
        driver.switch_to.window(window_no1)

        assert window_no1_title == driver.title
        time.sleep(1)
        driver.switch_to.window(window_no1)
        time.sleep(1)
        print(driver.title)
        driver.switch_to.window(window_no2)
        time.sleep(1)
        driver.switch_to.window(window_no3)
        time.sleep(1)
        driver.switch_to.window(window_no1)
        time.sleep(1)

    def tearDown(self):
        self.driver.close()
