from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import unittest


class JqueryUi(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def test_draggable(self):
        driver = self.driver
        driver.get("https://jqueryui.com/draggable/")
        iframe = driver.find_element_by_xpath("//iframe[@class='demo-frame']")
        driver.switch_to.frame(iframe)
        drag = driver.find_element_by_xpath("//div[@id='draggable']")
        action = ActionChains(driver)
        action.drag_and_drop_by_offset(drag, 0, 30).perform()

    def test_droppable(self):
        driver = self.driver
        driver.get("https://jqueryui.com/droppable/")
        iframe = driver.find_element_by_xpath("//iframe[@class='demo-frame']")
        driver.switch_to.frame(iframe)
        drag = driver.find_element_by_xpath("//div[contains(.,'Drag me to my target')]")
        drop = driver.find_element_by_xpath("//div[contains(.,'Drop here')]")
        action = ActionChains(driver)
        action.drag_and_drop(drag, drop).perform()

    def test_resizable(self):
        driver = self.driver
        driver.get("https://jqueryui.com/resizable/")
        iframe = driver.find_element_by_xpath("//iframe[@class='demo-frame']")
        driver.switch_to.frame(iframe)
        resizebox = driver.find_element_by_xpath(
            "//div[@class='ui-resizable-handle ui-resizable-se ui-icon ui-icon-gripsmall-diagonal-se']"
        )
        action = ActionChains(driver)
        action.click_and_hold(resizebox).drag_and_drop_by_offset(resizebox, 30, 80).perform()

    def test_selectable(self):
        driver = self.driver
        driver.get("https://jqueryui.com/selectable/")
        iframe = driver.find_element_by_xpath("//iframe[@class='demo-frame']")
        driver.switch_to.frame(iframe)
        item_1 = driver.find_element_by_xpath("//li[contains(text(),'Item 1')]")
        item_3 = driver.find_element_by_xpath("//li[contains(text(),'Item 3')]")
        item_5 = driver.find_element_by_xpath("//li[contains(text(),'Item 5')]")
        action = ActionChains(driver)
        action.key_down(Keys.LEFT_CONTROL)\
            .click(item_1)\
            .click(item_3)\
            .click(item_5)\
            .key_up(Keys.LEFT_CONTROL)\
            .perform()

    def test_sortable(self):
        driver = self.driver
        driver.get("https://jqueryui.com/sortable/")
        iframe = driver.find_element_by_xpath("//iframe[@class='demo-frame']")
        driver.switch_to.frame(iframe)
        item_2 = driver.find_element_by_xpath("//li[contains(text(),'Item 2')]")
        item_4 = driver.find_element_by_xpath("//li[contains(text(),'Item 4')]")
        item_6 = driver.find_element_by_xpath("//li[contains(text(),'Item 6')]")
        action = ActionChains(driver)
        action.click_and_hold(item_2).drag_and_drop_by_offset(item_2, 0, 50).perform()
        action.click_and_hold(item_4).drag_and_drop_by_offset(item_4, 0, 50).perform()
        action.click_and_hold(item_6).drag_and_drop_by_offset(item_6, 0, 50).perform()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()