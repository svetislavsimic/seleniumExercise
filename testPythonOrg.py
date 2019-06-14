import unittest
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time

class TestPythonOrg(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def testSearch(self):
        self.driver.get("http://www.python.org")
        assert "Python" in self.driver.title
        elem = self.driver.find_element_by_name("q")
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in self.driver.page_source

    def testNews(self):
        self.driver.get("http://www.python.org")
        assert "Python" in self.driver.title
        self.driver.find_element_by_id("news").click()
        assert "It will open News from around the Python world page" not in self.driver.page_source
        time.sleep(1)
    def tearDown(self):
        self.driver.close()
if __name__ == "__main__":
    unittest.main()
