from selenium.webdriver.common.by import By

from Pages.Base_Page import BasePage
from config.config import TestData


class HomePage(BasePage):

    CLASSES = (By.XPATH ,"//a[@class='ignoreTagStyle nav-item ']")
    SEARCH = (By.ID,"search")
    Moxie_Logo = (By.XPATH, "//span[@class='nav-moxie-logo']")


    def __init__(self, driver):
        super().__init__(driver)

    def verify_home_page_title(self, title):
        return self.get_title(title)

    def click_on_classes(self):
        self.click_element(self.CLASSES)

    def send_text_on_search(self,text):
        self.send_keys(self.SEARCH,text)

    def click_on_Moxie_Logo(self):
        self.click_element(self.Moxie_Logo)








