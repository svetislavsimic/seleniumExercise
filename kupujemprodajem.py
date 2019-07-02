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
from selenium.webdriver.support import expected_conditions as cond
from selenium.webdriver.common.by import By
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
        time.sleep(2)

        igrackeiigre = driver.find_element_by_xpath("//div[@data-value='1157']")
        driver.implicitly_wait(2)
        igrackeiigre.click()

        plisane = driver.find_element_by_xpath("//div[contains(@data-text,'Igračke | Plišane')]")
        driver.implicitly_wait(2)
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
        time.sleep(2)

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

        sledece = driver.find_element_by_xpath("//div[@class='slide-info-top-buttons']//div[@class='adFormPostButtonHolder']//input[@class='submit-button']")
        driver.implicitly_wait(10)
        sledece.click()
        driver.implicitly_wait(10)

        vidljivost = driver.find_element_by_xpath("//input[@id='data[promo_type]none']")
        WebDriverWait(driver, 10).until(cond.element_to_be_clickable((By.XPATH, "//input[@id='data[promo_type]none']")))
        vidljivost.click()

        sledece2 = driver.find_element_by_xpath("(//input[contains(@action-name,'adPromoNextButton')])[1]")
        sledece2.click()
        driver.implicitly_wait(5)

        ime = driver.find_element_by_xpath("//input[contains(@id,'personEdit')]")
        ime.click()
        ime.clear()
        ime.send_keys("Petar")

        prezime = driver.find_element_by_xpath("//input[contains(@id,'personLastNameEdit')]")
        prezime.click()
        prezime.clear()
        prezime.send_keys("Tasovac")

        mesto = driver.find_element_by_xpath("//input[contains(@name,'data[d_person_location]')]")
        mesto.click()
        mesto.clear()
        mesto.send_keys("Beograd")

        ulica = driver.find_element_by_xpath("//input[contains(@name,'data[d_person_address]')]")
        ulica.click()
        ulica.clear()
        ulica.send_keys("Borska 84")

        jmbg = driver.find_element_by_xpath("//input[contains(@name,'data[d_jmbg]')]")
        jmbg.click()
        jmbg.clear()
        jmbg.send_keys("2311999710274")

        time.sleep(3)




    def tearDown(self):
        self.driver.close()