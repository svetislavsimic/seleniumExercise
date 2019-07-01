from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/tooltip/")
time.sleep(5)
item = driver.find_element_by_id("age")
actualTitle=item.get_attribute("title")
assert actualTitle=="We ask for your age only for statistical purposes."
time.sleep(3)
driver.quit()