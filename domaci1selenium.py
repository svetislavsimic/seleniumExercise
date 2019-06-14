from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title
elm = webdriver.Chrome.find_element_by_xpath(driver, "//body[@id='homepage']/div[@id='touchnav-wrapper']/header[@class='main-header']/div[@class='container']/nav[@id='mainnav']/ul[@class='navigation menu']/li[@id='news']/a[1]")
elm.click()
assert "Our Blogs | Python.org" in driver.title
time.sleep(5)
driver.close()