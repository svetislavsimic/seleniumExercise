from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title
news = driver.find_element_by_id("news")
news.click()
assert "It will open News from around the Python world page" not in driver.page_source
time.sleep(10)
#actions.move_to_element()
#actions.click(hidden_submenu)
#time.sleep(10)
#actions.perform()
#time.sleep(10)
driver.close()

