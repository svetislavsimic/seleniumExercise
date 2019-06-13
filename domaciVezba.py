import a as a
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title
Button = driver.find_element_by_xpath("//*[@id='dive-into-python']/ol/li[2]/a")
Button.click()
time.sleep(5)
driver.close()