import unittest
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import datetime
import calendar

class ToolsQa(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

#    def simaNestoKuca(self):
#        print("Zdravo svete!")

#    def test_search_in_python_org(self):
#        driver = self.driver
#        driver.get('http://www.toolsqa.com/automation-practice-form/')
#        s1 = Select(driver.find_element_by_id('continents'))
#        s1.select_by_visible_text('Europe')

    def test_personal_data(self):
         driver = self.driver
         driver.get('http://www.toolsqa.com/automation-practice-form/')
         first_name=driver.find_element_by_xpath("//input[@name='firstname']")
         first_name.clear()
         first_name.send_keys("Vera")
         time.sleep(1)
         last_name=driver.find_element_by_xpath("//input[@name='lastname']")
         last_name.clear()
         last_name.send_keys("Rakić")
         time.sleep(1)
         sex=driver.find_element_by_xpath("//input[@value='Female']")
         sex.click()
         time.sleep(1)
         years_of_experience=driver.find_element_by_xpath("//input[contains(@value,'7')]")
         years_of_experience.click()
         date_entry=driver.find_element_by_xpath("//input[@id='datepicker']")
         date_entry.send_keys(datetime.datetime.now().strftime("%d. %m. %Y."))
         time.sleep(1)
         profession1=driver.find_element_by_xpath("//input[@id='profession-0']")
         profession1.click()
         profession2=driver.find_element_by_xpath("//input[@id='profession-1']")
         profession2.click()
         automation_tool1=driver.find_element_by_xpath()
         automation_tool2 = driver.find_element_by_xpath()
         automation_tool3 = driver.find_element_by_xpath()

         # assert "No results found." in driver.page_source
         time.sleep(2)




#        for opt in s1.options:
#            print(opt.text)
#            s1.select_by_visible_text(opt.text)
#            time.sleep(10)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()