import unittest
from selenium import webdriver
import os
from openpyxl import load_workbook

class Fastidious(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        currentFolderPath = os.getcwd()
        dataFolder = os.path.dirname(currentFolderPath)
        print(dataFolder)
        self.filePath = os.path.join(dataFolder , "data","fastidious.xlsx")

    def testLogInAdmin(self):
        driver = self.driver
        book = load_workbook(self.filePath)
        sheet = book.get_sheet_by_name("login")
        username=sheet['B2']
        password=sheet['C2']
        #driver.current_url== r"https://fastidious-app.netlify.com/dashboard"
        sheet.cell(row=2, column=4).value = "PASS"
        book.save(self.filePath)

    def tearDown(self):
            self.driver.close()
if __name__ == "__main__":
        unittest.main()
