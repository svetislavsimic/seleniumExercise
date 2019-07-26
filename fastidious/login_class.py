class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        un = self.driver.find_element_by_xpath("//input[contains(@name,'email')]")
        un.send_keys(username)

    def setPassword(self, password):
        pw = self.driver.find_element_by_xpath("//input[@name='password']")
        pw.send_keys(password)

    def login(self):
        libutton = self.driver.find_element_by_xpath("//button[@type='submit']")
        libutton.click()