import unittest
from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep


class Guru99(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        sleep(2)

    def testCountry(self):
        driver = self.driver
        driver.get('http://demo.guru99.com/test/newtours/register.php')
        selektiraj = Select(driver.find_element_by_name('country'))
        sleep(2)

        selektiraj.select_by_visible_text('BARBADOS')
        sleep(2)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()