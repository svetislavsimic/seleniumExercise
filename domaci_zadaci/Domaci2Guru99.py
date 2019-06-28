from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest as ut
from selenium.webdriver.support.select import Select
import time

class Guru99(ut.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_Barbados(self):
        driver = self.driver
        driver.get("http://demo.guru99.com/test/newtours/register.php")
        sel = Select(driver.find_element_by_xpath("//select[@name='country']"))
        sel.select_by_visible_text("BARBADOS")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    ut.main()
