import unittest
from selenium import webdriver
from time import sleep


class BlicTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

        '''1. Otvorite stranicu blic.rs
           Nadjite link "Svet"
           Otvorite taj link u novom tabu
           Otvorite prvu vest iz taba Svet'''

    def test_blic_svet(self):
        driver = self.driver
        driver.get("https://www.blic.rs/")
        driver.maximize_window()
        blic_home = driver.window_handles[0]

        for svet in driver.find_elements_by_xpath("//a[@href='/vesti/svet'][contains(.,'Svet')]"):
            svet.get_attribute('href')

        driver.execute_script("window.open('svet')")
        blic_svet = driver.window_handles[1]
        driver.switch_to.window(blic_svet)
        sleep(3)

        prva_vest = driver.find_element_by_xpath("//div[2]//section[1]//article[1]//div[1]")
        prva_vest.click()
        sleep(3)

    '''2. Otvorite Blic Kliknite na dugme Share '''

    def test_share(self):
        driver = self.driver
        driver.get("https://www.blic.rs/")
        driver.maximize_window()
        share_btn = driver.find_element_by_xpath("(//a[@href='#'][contains(.,'Share')])[4]")
        share_btn.click()
        sleep(3)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()