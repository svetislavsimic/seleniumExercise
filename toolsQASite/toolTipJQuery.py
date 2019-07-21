from selenium import webdriver
from selenium.webdriver import ActionChains
import time


baseUrl = "http://demo.guru99.com/test/tooltip.html"
driver = webdriver.Chrome()
expectedTooltip = "What's new in 3.2"
driver.get(baseUrl)

download = driver.find_element_by_xpath(".//*[@id='download_now']")
action_chains = ActionChains(driver)
action_chains.move_to_element(download).perform()
time.sleep(2)
toolTipElement = driver.find_element_by_xpath(".//*[@class='box']//div/a")
actualTooltip = toolTipElement.get_attribute("text")
assert  actualTooltip == expectedTooltip
print("Actual Title of Tool Tip  " + actualTooltip)
driver.close()