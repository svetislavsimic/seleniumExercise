import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class PythonOrg(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def testSearch(self):
        driver = self.driver
        driver.get("http://www.python.org")
        assert "Python" in driver.title
        elem = driver.find_element_by_name("q")
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source


    def testNews(self):
        driver = self.driver
        driver.get("http://www.python.org")
        assert "Python" in driver.title
        driver.find_element_by_id("news").click()
        assert "It will open News from around the Python world page" not in driver.page_source
        time.sleep(1)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()