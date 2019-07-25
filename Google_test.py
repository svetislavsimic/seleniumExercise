import unittest
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC

class GoogleTesting(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()


    def testGoogleFeelingLucky(self):
         driver = self.driver
         driver.get("https://www.google.com/ncr")
         driver.maximize_window()
         feeling_lucky=driver.find_element_by_xpath("(//input[@jsaction='sf.lck'])[2]")
         feeling_lucky.click()
         time.sleep(2)

         assert 'Jun 21, 2019' in driver.page_source
         time.sleep(2)




    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()