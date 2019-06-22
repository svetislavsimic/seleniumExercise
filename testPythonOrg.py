from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.select import Select
import time

class PythonOrg(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        #assert "Python" in driver.title
        elem = driver.find_element_by_name("q")
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        #assert "No results found." in driver.page_source
        time.sleep(2)

    def testNews(self):
        driver = self.driver
        driver.get("http://www.python.org")
        #assert "Python" in driver.title
        news = driver.find_element_by_id("news")
        news.click()
        #assert "It will open News from around the Python world page" not in driver.page_source
        time.sleep(2)

    def tearDown(self):
            self.driver.close()

if __name__ == "__main__":
    unittest.main()