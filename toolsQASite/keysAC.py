from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()
driver.get("http://www.teachmeselenium.com/automation-practice")
driver.maximize_window()

action_chains = ActionChains(driver)

#Type by pressing SHIFT
driver.find_element_by_id("firstname").click()
action_chains.key_down(Keys.SHIFT)
action_chains.send_keys("testuser")
action_chains.key_up(Keys.SHIFT)
action_chains.perform()
time.sleep(2)

#Ctrl-a
action_chains.key_down(Keys.LEFT_CONTROL).send_keys("a").key_up(Keys.LEFT_CONTROL).perform()
time.sleep(2)
#Ctrl-c
action_chains.key_down(Keys.LEFT_CONTROL).send_keys("c").key_up(Keys.LEFT_CONTROL).perform()
time.sleep(2)

#Press TAB
action_chains.send_keys(Keys.TAB).perform()
time.sleep(2)

#Ctrl-v
action_chains.key_down(Keys.LEFT_CONTROL).send_keys("v").key_up(Keys.LEFT_CONTROL).perform()
time.sleep(2)
driver.quit()