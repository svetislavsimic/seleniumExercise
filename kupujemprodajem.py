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
from selenium.webdriver.common.action_chains import ActionChains
class kupujemprodajem(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()


    def testKP(self):
        driver = self.driver
        driver.get("https://www.kupujemprodajem.com/")

        postavi_oglas = driver.find_element_by_xpath("//a[@class='bigLink submitAd']")
        postavi_oglas.click()

        emailentry = driver.find_element_by_xpath("(//input[@name='data[email]'])[1]")
        emailentry.click()
        emailentry.send_keys("petarpeca99@gmail.com")

        passwordentry = driver.find_element_by_xpath("//input[@type='password']")
        passwordentry.click()
        passwordentry.send_keys("novalozinka123")

        loginbutton = driver.find_element_by_xpath("(//input[contains(@name,'submit[login]')])[2]")
        loginbutton.click()

        rucno = driver.find_element_by_xpath("//input[@id='data[ad_kind]goods']")
        rucno.click()

        igrackeiigre = driver.find_element_by_xpath("//div[@class='uiMenuItem'][contains(.,'Igračke i igre')]")
        igrackeiigre.click()

        plisane = driver.find_element_by_xpath("//div[contains(@data-text,'Igračke | Plišane')]")
        plisane.click()

        time.sleep(2)
        naslovoglasa = driver.find_element_by_xpath("//input[contains(@id,'data[name]')]")
        naslovoglasa.click()
        naslovoglasa.clear()
        naslovoglasa.send_keys("Plisani Medved")

        stanje = driver.find_element_by_xpath("//input[contains(@id,'data[condition]as-new')]")
        stanje.click()

        cena = driver.find_element_by_xpath("//input[contains(@id,'price_number')]")
        cena.click()
        cena.clear()
        cena.send_keys("1000000")

        valuta = driver.find_element_by_xpath("//input[@id='currency_eur']")
        valuta.click()

        # driver.implicitly_wait(10)
        # tekstoglasa = driver.find_element_by_xpath("//body[@id='tinymce']")
        # tekstoglasa.click()
        # tekstoglasa.clear()
        # tekstoglasa.send_keys("Prodajem Plisanog Medveda")
        action = ActionChains(driver)
        action.send_keys(Keys.TAB)
        action.send_keys(Keys.TAB)
        action.send_keys(Keys.TAB)
        action.send_keys("prodajem plisanog medveda")
        action.perform()

        sledece = driver.find_element_by_xpath("(//input[contains(@action-name,'adInfoNextButton')])[1]")
        sledece.click()

        vidljivost = driver.find_element_by_xpath("//input[@id='data[promo_type]none']")
        vidljivost.click()

        sledece2 = driver.find_element_by_xpath("(//input[contains(@action-name,'adPromoNextButton')])[1]")
        sledece2.click()


    def tearDown(self):
        self.driver.close()