import unittest
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC

class SwitchingTabTesting(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()


    def testWindowSwitching(self):
        # open the first window
        driver = self.driver

        driver.get("https://www.blic.rs")
        driver.maximize_window()
        # get the window handle after the window has opened
        blic_tab = driver.window_handles[0]

        blic_tab_title = driver.title

        # open a new window
        driver.execute_script("window.open('https://instagram.com')")

        # get the window handle after a new window has opened
        instagram_tab = driver.window_handles[1]

        # switch on to new child window
        driver.switch_to.window(instagram_tab)
        time.sleep(10)

        facebook_tab_title = driver.title

        driver.execute_script("window.open('https://facebook.com')")

        # get the window handle after a new window has opened
        facebook_tab = driver.window_handles[2]

        # switch on to new child window
        driver.switch_to.window(facebook_tab)
        time.sleep(10)

        instagram_tab_title = driver.title

        # Compare and verify that main window and child window title don't match
#        assert blic_tab_title != instagram_tab_title
        # switch back to original window
        driver.switch_to.window(blic_tab)

        # Verify that the title now match
 #       assert blic_tab_title == driver.title

        print(driver.title)
        #driver.close()
        driver.switch_to.window(instagram_tab)
        time.sleep(3)

    def tearDown(self):
        self.driver.close()