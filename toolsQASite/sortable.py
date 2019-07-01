from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/sortable/")
action_chains = ActionChains(driver)
time.sleep(5)
item1 = driver.find_element_by_xpath("//li[contains(text(),'Item 1')]")
action_chains.drag_and_drop_by_offset(item1,0,40).perform()

time.sleep(7)
driver.quit()