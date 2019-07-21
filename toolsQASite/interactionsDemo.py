from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/draggable/");
time.sleep(5)
dragable = driver.find_element_by_xpath("//p[contains(text(),'Drag me around')]")
time.sleep(5)
action_chains = ActionChains(driver)
action_chains.drag_and_drop_by_offset(dragable, 50, 30).perform()
time.sleep(5)
driver.quit()