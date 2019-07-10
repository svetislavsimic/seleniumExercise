import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
import time

class JQueryUI(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def testDroppable(self):
        driver = self.driver
        driver.get("https://jqueryui.com/droppable/")
        time.sleep(5)
        driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
        dragable = driver.find_element_by_id('draggable')
        dropable = driver.find_element_by_id('droppable')
        action_chain = ActionChains(driver)
        action_chain.drag_and_drop(dragable,dropable).perform()
        time.sleep(3)

    def tearDown(self):
        self.driver.close()