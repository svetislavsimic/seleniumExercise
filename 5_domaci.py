from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest


class BlicTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

        '''Testirati blic i iskoristiti:
        title_is
        title_contains
        element_to_be_clickable'''

    def test_click(self):
        driver = self.driver
        driver.get("https://www.blic.rs/")

        wait = WebDriverWait(driver, 10)

        element = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//a[@href='/zabava']")))
        element.click

    def test_title_is(self):
        driver = self.driver
        driver.get("https://www.blic.rs/")
        wait = WebDriverWait(driver, 10)
        zanimljivosti = driver.find_element_by_xpath("//a[@href='/slobodno-vreme/zanimljivosti']")
        zanimljivosti.click()
        naslov = driver.title
        wait.until(EC.title_is(naslov))
        putovanja = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//a[contains(text(),'Putovanja')]")))
        putovanja.click()

    def test_title_contains(self):
        driver = self.driver
        driver.get("https://www.blic.rs/")
        wait = WebDriverWait(driver, 10)
        driver.find_element_by_xpath("//a[@href='/biznis'][contains(.,'Biznis')]").click()
        wait.until(EC.title_contains("Biznis"))


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()