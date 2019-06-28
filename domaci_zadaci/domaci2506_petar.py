import unittest
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as cond
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
class BlicExplicitWaitTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()


    def testTitleIs(self):
        driver = self.driver
        driver.get('https://www.blic.rs/')
        drustvo = driver.find_element_by_xpath("//a[@href='/vesti/drustvo']")
        drustvo.click()
        drustvotitle = driver.title
        WebDriverWait(driver, 10).until(cond.title_is(drustvotitle))
        clanak = driver.find_element_by_xpath("/html[1]/body[1]/main[1]/div[1]/section[1]/div[2]/section[1]/article[1]/div[1]/h3[1]/a[1]")
        clanak.click()
    def testTitleContains(self):
        driver = self.driver
        driver.get('https://www.blic.rs/')
        drustvo = driver.find_element_by_xpath("//a[@href='/vesti/drustvo']")
        drustvo.click()
        WebDriverWait(driver, 10).until(cond.title_contains("Blic"))
        clanak = driver.find_element_by_xpath("/html[1]/body[1]/main[1]/div[1]/section[1]/div[2]/section[1]/article[1]/div[1]/h3[1]/a[1]")
        clanak.click()
    def testElementToBeClickable(self):
        driver = self.driver
        driver.get("https://www.blic.rs/")
        drustvo = driver.find_element_by_xpath("//a[@href='/vesti/drustvo']")
        WebDriverWait(driver, 10).until(cond.element_to_be_clickable((By.XPATH, "//a[@href='/vesti/drustvo']")))
        drustvo.click()



    def tearDown(self):
        self.driver.close()