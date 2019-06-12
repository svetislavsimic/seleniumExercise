from selenium import webdriver
#from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title
elm = webdriver.Chrome.find_element_by_xpath(driver, "//body[@id='homepage']/div[@id='touchnav-wrapper']/header[@class='main-header']/div[@class='container']/nav[@id='mainnav']/ul[@class='navigation menu']/li[@id='news']/a[1]")
elm.click()
assert "No results found." not in driver.page_source
