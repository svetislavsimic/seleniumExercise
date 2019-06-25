import unittest
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urljoin
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait



class BlicTesting(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()


    def testBlicSvet(self):
        driver = self.driver
        blic_url = "https://www.blic.rs"
        driver.get(blic_url)
        driver.maximize_window()
        blic_naslovna = driver.window_handles[0]
        blic_naslovna_title = driver.title
        time.sleep(2)
        print(driver.title)

        share_button = driver.find_element_by_xpath("(//i[contains(@class,'fa fa-facebook-official')])[5]")
        share_button.click()

#        share_button = driver.find_element_by_xpath("//button[@type='submit'][contains(@id,'5')][contains('Share')]")
         #share_button.click()



    def tearDown(self):
        self.driver.close()