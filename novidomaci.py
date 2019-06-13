from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title
tab = driver.find_element_by_xpath("//*[@id='news']/a")
tab.click()
time.sleep(10)
driver.close()