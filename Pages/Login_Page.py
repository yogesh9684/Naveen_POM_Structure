import pytest
from selenium.webdriver.common.by import By
from Pages.Base_Page import BasePage
from config.config import TestData


'''Login Page with defined Locators and Methods'''

class LoginPage(BasePage):

    Email_Field = (By.XPATH, '//input[@type="email"]')
    Password_Filed = (By.XPATH,'//input[@name="password"]')
    Click_On_Sign_In = (By.XPATH,'//button[@type="submit"]')


    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get(TestData.URL)
        self.driver.maximize_window()

    def login_page_title(self,title):
        return self.get_title(title)

    def make_login(self,username,password):
        self.send_keys(self.Email_Field , username)
        self.send_keys(self.Password_Filed , password)
        self.click_element(self.Click_On_Sign_In)