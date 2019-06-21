import unittest
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC

class FacebookTesting(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()


    def testWindowSweetching(self):
        # open the first window
        driver = self.driver

        driver.get("http://www.facebook.com")
        driver.maximize_window()
        # get the window handle after the window has opened
        window_before = driver.window_handles[0]

        window_before_title = driver.title

        # open a new window
        driver.execute_script("window.open('http://www.twitter.com', 'new window')")

        # get the window handle after a new window has opened
        window_after = driver.window_handles[1]

        # switch on to new child window
        driver.switch_to.window(window_after)
        time.sleep(10)

        window_after_title = driver.title

        # Compare and verify that main window and child window title don't match
        assert window_before_title != window_after_title
        # switch back to original window
        driver.switch_to.window(window_before)

        # Verify that the title now match
        assert window_before_title == driver.title

        print(driver.title)
        #driver.close()
        driver.switch_to.window(window_after)
        time.sleep(3)

    def tearDown(self):
        self.driver.close()