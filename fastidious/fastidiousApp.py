import unittest
from selenium import webdriver
import os
from openpyxl import load_workbook
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class Fastidious(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        working_folder = os.getcwd()
        data_folder = os.path.dirname(working_folder)
        print(data_folder)
        self.filePath = os.path.join(data_folder, "data", "fastidious.xlsx")

    def testLogInAdmin(self):
        driver = self.driver
        book = load_workbook(self.filePath)
        sheet = book.get_sheet_by_name("Login")
        username = sheet['B2'].value
        password = sheet['C2'].value
        driver.get("https://fastidious-app.netlify.com")
        wait = WebDriverWait(driver, 10)
        # driver.current_url== r"https://fastidious-app.netlify.com/dashboard"

        user_field = driver.find_element_by_xpath("//input[contains(@name,'email')]")
        password_field = driver.find_element_by_xpath("//input[contains(@name,'password')]")
        login_btn = driver.find_element_by_xpath("//button[@type='submit']")

        user_field.send_keys(username)
        password_field.send_keys(password)
        login_btn.click()

        wait.until(EC.url_contains("https://fastidious-app.netlify.com/dashboard"))

        assert driver.current_url == r"https://fastidious-app.netlify.com/dashboard"
        sheet.cell(row=2, column=4).value = "PASS"
        book.save(self.filePath)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
