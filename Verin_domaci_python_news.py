from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title
driver.find_element_by_id("news").click()
assert "It will open News from around the Python world page" not in driver.page_source
time.sleep(10)
driver.close()

