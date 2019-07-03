import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

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
        username.send_keys("nevena.miocinovic@gmail.com")

        password = driver.find_element_by_xpath("//input[@type='password']")
        password.clear()
        password.send_keys("testkupujemprodajem")

        logIn = driver.find_element_by_xpath("//input[@value='Ulogujte se']")
        logIn.click()

        usluga = driver.find_element_by_xpath("//input[@id='data[ad_kind]service']")
        usluga.click()
        time.sleep(3)

        poducavanje = driver.find_element_by_xpath("//div[@data-value='1412']")
        poducavanje.click()


        grupa = driver.find_element_by_xpath("//div[@data-value='1462']")
        grupa.click()

        naslovoglasa = driver.find_element_by_xpath("//input[contains(@id,'data[name]')]")
        naslovoglasa.click()
        naslovoglasa.clear()
        naslovoglasa.send_keys("Časovi manuelnog testiranja")


        cena = driver.find_element_by_xpath("//input[contains(@id,'price_number')]")
        cena.click()
        cena.clear()
        cena.send_keys("100")

        valuta = driver.find_element_by_xpath("//input[@id='currency_eur']")
        valuta.click()
        driver.implicitly_wait(5)

        action = ActionChains(driver)
        action.send_keys(Keys.TAB)
        action.send_keys(Keys.TAB)
        action.send_keys(Keys.TAB)
        action.send_keys("Povoljni časovi manuelnog testiranja")
        action.perform()

        mesto = driver.find_element_by_xpath("(//span[contains(.,'Izaberite')])[13]")
        mesto.click()

        mestoizbor = driver.find_element_by_xpath("// div[ @class ='uiMenuItem'][contains(., 'Borča')]")
        mestoizbor.click()

        ime = driver.find_element_by_xpath("//input[contains(@id,'data[owner]')]")
        ime.click()
        ime.clear()
        ime.send_keys("Nevena")

        sledece = driver.find_element_by_xpath("//div[@class='slide-info-top-buttons']//div[@class='adFormPostButtonHolder']//input[@class='submit-button']")
        sledece.click()


    def tearDown(self):
         self.driver.close()