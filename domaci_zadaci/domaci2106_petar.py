import unittest
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains

class TestPythonOrg(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def testSearch(self):
        driver = self.driver
        driver.get("https://www.blic.rs/")
        svetelm = driver.find_element_by_xpath("(//a[contains(.,'Svet')])[1]")
        svethref = svetelm.get_attribute('href')
        driver.execute_script("window.open('{}')".format(svethref))
        driver.implicitly_wait(10)
        clanakelm = driver.find_element_by_xpath("/html[1]/body[1]/main[1]/div[1]/section[1]/div[2]/section[1]/article[1]/div[1]/h3[1]/a[1]")
        print(clanakelm.get_attribute("href"))

    def testNews(self):
        driver = self.driver
        driver.get("https://www.blic.rs/")
        a = driver.find_element_by_xpath("(//a[@href='#'][contains(.,'Share')])[7]")
        action = ActionChains(driver)
        action.move_to_element(a).perform()
        a.click()
    def tearDown(self):
        self.driver.close()
if __name__ == "__main__":
    unittest.main()