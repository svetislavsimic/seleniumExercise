from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/resizable/")
action_chains = ActionChains(driver)
time.sleep(5)
resizeable = driver.find_element_by_xpath("//div[@class='ui-resizable-handle ui-resizable-se ui-icon ui-icon-gripsmall-diagonal-se']")
action_chains.click_and_hold(resizeable).drag_and_drop_by_offset(resizeable,60,70)
action_chains.perform()
time.sleep(5)
driver.quit()