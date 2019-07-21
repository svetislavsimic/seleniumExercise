import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as cond
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class domaci(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def testGmail(self):
        driver = self.driver
        driver.get("https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB")
        driver.implicitly_wait(5)
        username = driver.find_element_by_id("identifierId")
        username.send_keys("petarpeca1999@gmail.com")
        username.send_keys(Keys.ENTER)

        time.sleep(3.5)
        password = driver.find_element_by_xpath("//input[@type='password']")
        password.send_keys("mavrenfein024")
        password.send_keys(Keys.ENTER)

        driver.implicitly_wait(5)
        notifications = driver.find_element_by_xpath("//div[contains(@class,'bBe')]")
        notifications.click()

        driver.implicitly_wait(3)
        compose = driver.find_element_by_xpath("//div[contains(@gh,'cm')]")
        compose.click()

        action = ActionChains(driver)
        action.send_keys("petarpeca1999@gmail.com")
        action.perform()

        subject = driver.find_element_by_xpath("//input[contains(@id,':qt')]")
        subject.send_keys("Whatever")

        send = driver.find_element_by_xpath("//div[contains(@id,':qj')]")
        send.click()


        time.sleep(7)
    def testYoutube(self):
        driver = self.driver
        driver.get("https://www.youtube.com/")

        search = driver.find_element_by_xpath("//input[contains(@id,'search')]")
        search.send_keys("in flames the quiet place")
        search.send_keys(Keys.ENTER)

        driver.implicitly_wait(3)
        tqp = driver.find_element_by_xpath("//a[@title='In Flames - The Quiet Place']")
        tqp.click()

        driver.implicitly_wait(3)
        progressbar = driver.find_element_by_xpath("//div[@class='ytp-progress-bar-padding']")
        time.sleep(3)
        action2 = ActionChains(driver)
        for item in range(1, 21):
            action2.send_keys(Keys.ARROW_UP)
        action2.perform()
        action = ActionChains(driver)
        action.move_to_element(progressbar)
        action.drag_and_drop_by_offset(progressbar, -330, 0)
        action.perform()


        time.sleep(3)
    def testGitlabNoInfo(self):
        driver = self.driver
        driver.get("https://gitlab.com/users/sign_in")

        signinbutton = driver.find_element_by_xpath("//input[contains(@value,'Sign in')]")
        signinbutton.click()

        assert "This field is required." in driver.page_source
        time.sleep(1)
    def testUsernameOnly(self):
        driver = self.driver
        driver.get("https://gitlab.com/users/sign_in")

        signinbutton = driver.find_element_by_xpath("//input[contains(@value,'Sign in')]")
        username = driver.find_element_by_xpath("//input[contains(@id,'user_login')]")
        username.send_keys("petarpeca99@gmail.com")
        signinbutton.click()
        assert "This field is required." in driver.page_source
        time.sleep(1.5)
    def testPasswordOnly(self):
        driver = self.driver
        driver.get("https://gitlab.com/users/sign_in")

        signinbutton = driver.find_element_by_xpath("//input[contains(@value,'Sign in')]")
        password = driver.find_element_by_xpath("//input[@id='user_password']")
        password.send_keys("12345678")
        signinbutton.click()
        assert "This field is required." in driver.page_source
        time.sleep(1.5)
    #Invalid Login or password.
    def testFakeInfo(self):
        driver = self.driver
        driver.get("https://gitlab.com/users/sign_in")

        signinbutton = driver.find_element_by_xpath("//input[contains(@value,'Sign in')]")
        username = driver.find_element_by_xpath("//input[contains(@id,'user_login')]")
        username.send_keys("petarpeca99@gmail.com")
        password = driver.find_element_by_xpath("//input[@id='user_password']")
        password.send_keys("12345678")
        signinbutton.click()
        assert "Invalid Login or password." in driver.page_source
        time.sleep(1.5)
    def testCorrectInfo(self):
        driver = self.driver
        driver.get("https://gitlab.com/users/sign_in")

        signinbutton = driver.find_element_by_xpath("//input[contains(@value,'Sign in')]")
        username = driver.find_element_by_xpath("//input[contains(@id,'user_login')]")
        username.send_keys("petarpeca99@gmail.com")
        password = driver.find_element_by_xpath("//input[@id='user_password']")
        password.send_keys("mavrenfein024")
        signinbutton.click()
        driver.implicitly_wait(2)
        assert "Welcome to GitLab" in driver.page_source
        time.sleep(1.5)
    def tearDown(self):
        self.driver.close()

