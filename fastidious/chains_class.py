class ChainsPage:
    def __init__(self, driver):
        self.driver = driver

    def setChainName(self, name):
        cn = self.driver.find_element_by_xpath("//input[@name='name']")
        cn.send_keys(name)

    def setDescription(self, description):
        desc = self.driver.find_element_by_xpath("//input[@name='description']")
        desc.send_keys(description)

    def setPhone(self, phone):
        pho = self.driver.find_element_by_xpath("//input[@name='phone']")
        pho.send_keys(phone)

    def addChain(self):
        add = self.driver.find_element_by_xpath("//button[@type='submit']")
        add.click()