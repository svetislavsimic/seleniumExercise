import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as cond
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException
from selenium.common.exceptions import StaleElementReferenceException
import time

class KupujemProdajem(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver,10)

    def testPostAd(self):
        driver = self.driver
        driver.get("https://www.kupujemprodajem.com/index.php")
        postaviOglas = driver.find_element_by_xpath("//a[contains(@class,'bigLink submitAd')]")
        postaviOglas.click()
        username = driver.find_element_by_xpath("(//input[@name='data[email]'])[1]")
        username.clear()
        username.send_keys("santaleda@yahoo.com")
        password = driver.find_element_by_xpath("//input[@type='password']")
        password.clear()
        password.send_keys("sl10456")
        logIn = driver.find_element_by_xpath("//input[@value='Ulogujte se']")
        logIn.click()
        usluga = driver.find_element_by_xpath("//input[@id='data[ad_kind]service']")
        usluga.click()
        #*****
        time.sleep(5)
        a = driver.find_element_by_xpath("(//span[@action-name='label'])[3]")
        a.click()
        time.sleep(1)
        a.click()
        time.sleep(1)
        poducavanje = driver.find_element_by_xpath("//div[@data-value='1412']")
        ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,ElementNotVisibleException)
        WebDriverWait(driver, 10, ignored_exceptions=ignored_exceptions) \
            .until(cond.visibility_of(poducavanje))
        poducavanje.click()
        grupa = driver.find_element_by_xpath("//div[@data-value='1462']")
        grupa.click()
        naslovOglasa = driver.find_element_by_xpath("//input[@id='data[name]']")
        self.wait.until(cond.visibility_of(naslovOglasa))

        naslovOglasa.clear()
        naslovOglasa.send_keys("Casovi makroekonomije za studente")
        cenaPoducavanja = driver.find_element_by_xpath("//input[@id='price_number']")
        cenaPoducavanja.send_keys(2000)
        dinari = driver.find_element_by_xpath("//input[@id='currency_rsd']")
        dinari.click()
        action_chains = ActionChains(driver)
        action_chains.key_down(Keys.TAB)
        action_chains.key_down(Keys.TAB)
        action_chains.send_keys("Povoljni casovi")
        action_chains.perform()
        time.sleep(5)

    def tearDown(self):
        self.driver.close()