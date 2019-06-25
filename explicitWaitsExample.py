from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as cond
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
import os
import time

driver = webdriver.Chrome()
driver.maximize_window()
location = os.path.join(os.getcwd(),"js_code","explicitWaitsExample.html")
driver.get(location)

# Press the "Alert" button to demonstrate the Simple Alert
button = driver.find_element_by_name('alert')
button.click()

try:
    # Wait as long as required, or maximum of 10 sec for alert to appear
    WebDriverWait(driver, 10).until(cond.alert_is_present())
    time.sleep(2)
    # Change over the control to the Alert window
    obj = driver.switch_to.alert

    # Retrieve the message on the Alert window
    msg = obj.text
    print("Alert shows following message: " + msg)

    # Use the accept() method to accept the alert
    obj.accept()

except (NoAlertPresentException, TimeoutException) as py_ex:
    print("Alert not present")
    print(py_ex)
    print(py_ex.args)
finally:
    driver.quit()