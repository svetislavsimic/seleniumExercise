#Kreirati klasu Guru99 koja je izvedena iz klase TestCase
#i otvoriti stranicu:
#http://demo.guru99.com/test/newtours/register.php
#U klasi Guru99 implementirati metod testCountry u kom cete
#selektovati Barbados kao zemlju iz liste ponudjenih zemalja.

import unittest
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

class Guru99(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()


    def test_Country(self):
        driver = self.driver
        driver.get('http://demo.guru99.com/test/newtours/register.php')
        select_County= Select(driver.find_element_by_name('country'))

        select_County.select_by_value("BARBADOS")
        time.sleep(10)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
