from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/watch?v=cEnJDaqT3-0")
action_chains = ActionChains(driver)
time.sleep(100)
item1 = driver.find_element_by_xpath("//div[@class='ytp-volume-panel']")
action_chains.click_and_hold(item1).move_by_offset(-20,0)
action_chains.release()
action_chains.perform()
time.sleep(10)
driver.quit()