import unittest
from selenium import webdriver
import os
from openpyxl import load_workbook
import time

class Fastidious(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        currentFolderPath = os.getcwd()
        dataFolder = os.path.dirname(currentFolderPath)
        print(dataFolder)
        self.filePath = os.path.join(dataFolder , "data","fastidious.xlsx")
        self.driver.get("https://fastidious-app.netlify.com/login")

    def testLogInAdmin(self):
        driver = self.driver
        book = load_workbook(self.filePath)
        sheet = book.get_sheet_by_name("login")
        username = sheet['B2'].value
        password = sheet['C2'].value
        usernameentry = driver.find_element_by_xpath("//input[@name='email']")
        usernameentry.send_keys(username)
        passwordentry = driver.find_element_by_xpath("//input[@name='password']")
        passwordentry.send_keys(password)

        loginbutton = driver.find_element_by_xpath("//button[@type='submit']")
        loginbutton.click()
        time.sleep(2)
        assert driver.current_url == r"https://fastidious-app.netlify.com/dashboard"
        sheet.cell(row=2, column=4).value = "PASS"
        book.save(self.filePath)
    def testIncorrectUsername(self):
        driver = self.driver
        book = load_workbook(self.filePath)
        sheet = book.get_sheet_by_name("login")
        username = sheet['B3'].value
        password = sheet['C3'].value
    def tearDown(self):
            self.driver.close()
if __name__ == "__main__":
        unittest.main()
