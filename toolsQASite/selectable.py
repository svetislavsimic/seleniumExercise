from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/selectable/")
action_chains = ActionChains(driver)
time.sleep(5)
item1 = driver.find_element_by_xpath("//li[contains(text(),'Item 1')]")
item4 = driver.find_element_by_xpath("//li[contains(text(),'Item 4')]")
action_chains.key_down(Keys.LEFT_CONTROL)
action_chains.click(item1)
action_chains.click(item4)
action_chains.key_up(Keys.LEFT_CONTROL)
action_chains.perform()
time.sleep(3)
driver.quit()