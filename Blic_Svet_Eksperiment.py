import unittest
from selenium import webdriver
import time

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urljoin



class FacebookTesting(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
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

        svet = driver.find_element_by_xpath("//a[@href='/vesti/svet']")
        svet_url = svet.get_attribute("href")
        svet_ceo_url = urljoin(blic_url,svet_url)
        driver.execute_script("window.open('{}')".format(svet_ceo_url))

        svet = driver.window_handles[1]
        driver.switch_to.window(svet)
        time.sleep(3)
        svet_title = driver.title
        print(driver.title)


        prva_vest_u_svetu = driver.find_element_by_xpath("/html[1]/body[1]/main[1]/div[1]/section[1]/div[2]/section[1]/article[1]/div[1]/h3[1]/a[1]")
        prva_vest_u_svetu_url = prva_vest_u_svetu.get_attribute("href")
        prva_vest_u_svetu_ceo_url = urljoin(svet_ceo_url, prva_vest_u_svetu_url)
        driver.execute_script("window.open('{}')".format(prva_vest_u_svetu_ceo_url))

        prva_vest_u_svetu = driver.window_handles[2]
        driver.switch_to.window(prva_vest_u_svetu)
        time.sleep(3)
        print(driver.title)
        prva_vest_u_svetu_title = driver.title


        driver.switch_to.window(svet)
        time.sleep(3)
        print(driver.title)


        treca_vest_u_svetu = driver.find_element_by_xpath("/html[1]/body[1]/main[1]/div[1]/section[1]/div[2]/section[1]/article[3]/div[1]/h3[1]/a[1]")
        treca_vest_u_svetu.click()
        time.sleep(3)
        treca_vest_u_svetu_title = driver.title
        print(driver.title)

        driver.switch_to.window(svet)
        time.sleep(3)
        print(driver.title)

        driver.switch_to.window(blic_naslovna)
        time.sleep(3)
        print(driver.title)

        # Compare and verify that main window and child window title don't match
        assert blic_naslovna_title != svet_title
        assert svet.title != prva_vest_u_svetu_title
        assert treca_vest_u_svetu_title != svet_title
        assert blic_naslovna_title == driver.title
        assert treca_vest_u_svetu_title != svet_title
        # switch back to original window


        # Verify that the title now match
        #assert blic_naslovna_title == driver.title




    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()