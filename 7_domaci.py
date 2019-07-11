from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import unittest
from time import sleep


class HomeWork(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_gmail(self):

        '''Log in with gmail acccount'''
        username = ""  # enter gmail account email
        password = ""  # enter gmail account password

        send_mail_to = ""  # enter recipient email address

        mail_subject = "Selenium mail"
        mail_message = "This email is automatically generated by Selenium Testing Tools"

        driver = self.driver
        driver.get("https://www.gmail.com")
        wait = WebDriverWait(driver, 10)

        '''Log in '''
        wait.until(EC.presence_of_element_located((By.NAME, "identifier"))).send_keys(username+Keys.ENTER)

        wait.until(EC.presence_of_element_located((
            By.XPATH, "//input[@name='password']"))).send_keys(password+Keys.ENTER)

        '''Compose and send'''
        wait.until(EC.presence_of_element_located((By.XPATH, "(//div[@tabindex='0'])[9]"))).click()

        wait.until(EC.presence_of_element_located((
            By.XPATH, "//textarea[contains(@aria-label,'To')]"))).send_keys(send_mail_to)

        wait.until(EC.presence_of_element_located((
            By.XPATH, "//input[contains(@aria-label,'Subject')]"))).send_keys(mail_subject)

        wait.until(EC.presence_of_element_located((
            By.XPATH, "//div[contains(@aria-label,'Message Body')]"))).send_keys(mail_message+Keys.TAB+Keys.ENTER)
        sleep(2)

    def test_youtube(self):
        driver = self.driver
        driver.get("https://www.youtube.com")
        wait = WebDriverWait(driver, 10)
        action = ActionChains(driver)

        search_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='search']")))
        search_field.send_keys("whorehouse blues" + Keys.ENTER)

        song = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Motorhead - Whorehouse Blues")))
        song.click()

        invideo = wait.until(EC.presence_of_element_located((By.XPATH, "//video[@class='video-stream html5-main-video']")))
        action.move_to_element(invideo)
        action.send_keys("f")
        action.perform()

        for i in range(19):
            action = action.send_keys(Keys.ARROW_UP)
        action.perform()

        for z in range(6):
            action = action.send_keys(Keys.ARROW_RIGHT)
        action.perform()
        sleep(180)

    def test_gitlab(self):
        driver = self.driver
        driver.get("https://gitlab.com/users/sign_in")
        wait = WebDriverWait(driver, 10)

        '''Log in with github account'''
        username = ""  # enter github account email
        password = ""  # enter  github password

        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@id='oauth-login-github']"))).click()
        email_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='login_field']")))
        email_field.send_keys(username)
        password_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='password']")))
        password_field.send_keys(password)
        driver.find_element_by_xpath("//input[@name='commit']").click()
        driver.find_element_by_xpath("//button[@id='js-oauth-authorize-btn']").click()
        accept_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn btn-success prepend-left-8")))
        accept_btn.click()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()