from selenium import webdriver
from time import sleep


driver = webdriver.Chrome()
driver.get("http://www.python.org")
driver.maximize_window()
assert "Python" in driver.title
sleep(2)
driver.find_element_by_id("news").click()
sleep(4)
driver.close()