from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/sortable/")
action_chains = ActionChains(driver)
time.sleep(5)
item1 = driver.find_element_by_xpath("//li[contains(text(),'Item 1')]")
item2 = driver.find_element_by_xpath("//li[contains(text(),'Item 3')]")
action_chains.click_and_hold(item1)
action_chains.move_to_element(item2).move_by_offset(0,5)
action_chains.release()
action_chains.perform()
time.sleep(7)
driver.quit()