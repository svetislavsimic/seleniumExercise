from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/droppable/");
time.sleep(5)
source = driver.find_element_by_xpath("//p[contains(text(),'Drag me to my target')]")
target = driver.find_element_by_xpath("//div[@id='droppable']")
time.sleep(5)
action_chains = ActionChains(driver)
action_chains.drag_and_drop(source, target).perform()
time.sleep(5)
driver.quit()