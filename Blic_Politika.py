import unittest
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urljoin



class FacebookTesting(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()


    def testBlicPolitika(self):
        # open the first window
        driver = self.driver
        blicUrl="https://www.blic.rs"
        driver.get(blicUrl)
        driver.maximize_window()
        blic_open = driver.window_handles[0]
        blic_open_title = driver.title
        time.sleep(2)

        politika_webElement = driver.find_element_by_xpath("//a[@href='/vesti/politika']")
        politikaUrl=politika_webElement.get_attribute("href")
        newUrl=urljoin(blicUrl,politikaUrl)
        driver.execute_script("window.open('{}')".format(newUrl))

        politika_tab = driver.window_handles[1]

        # switch on to new child window
        driver.switch_to.window(politika_tab)
        time.sleep(3)

        politika_tab_title = driver.title

        # Compare and verify that main window and child window title don't match
        #assert blic_open_title != politika_tab_title
        # switch back to original window
        driver.switch_to.window(blic_open)

        # Verify that the title now match
        #assert blic_open_title == driver.title

        print(driver.title)
        #driver.close()
        driver.switch_to.window(politika_tab)
        time.sleep(3)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()