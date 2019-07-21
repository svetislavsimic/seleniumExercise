from selenium import webdriver
from selenium.webdriver import ActionChains
import time


driver = webdriver.Chrome()
driver.get("https://www.imdb.com/")
time.sleep(3)
eleMenuShowtimes = driver.find_element_by_id("navTitleMenu")

action_chains = ActionChains(driver)
action_chains.move_to_element(eleMenuShowtimes)
time.sleep(3)
action_chains.click(driver.find_element_by_link_text("In Theaters"))
action_chains.perform()
time.sleep(3)
assert  "New Movies In Theaters" in driver.title

driver.quit()