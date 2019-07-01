import unittest
from selenium import webdriver
import time

class KupujemProdajem(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

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
        #WebDriverWait(driver, 10).until(cond.alert_is_present()) page loadded
        usluga = driver.find_element_by_xpath("//input[@id='data[ad_kind]service']")
        usluga.click()
        time.sleep(3)
        poducavanje = driver.find_element_by_xpath("//div[@data-value='1412']")
        poducavanje.click()
        grupa = driver.find_element_by_xpath("//div[@data-value='1462']")
        grupa.click()
        naslovOglasa = driver.find_element_by_xpath("//input[@id='data[name]']")


        time.sleep(5)

    def tearDown(self):
         self.driver.close()