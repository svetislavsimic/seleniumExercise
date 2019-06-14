import unittest
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

class ToolsQa(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def simaNestoKuca(self):
        print("Zdravo svete!")

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get('http://www.toolsqa.com/automation-practice-form/')
        s1 = Select(driver.find_element_by_id('continents'))

        s1.select_by_visible_text('Europe')

        for opt in s1.options:
            print(opt.text)
            s1.select_by_visible_text(opt.text)
            time.sleep(10)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()