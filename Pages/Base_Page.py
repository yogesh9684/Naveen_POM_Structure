from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

'''This Class is Parent of All the Pages'''
''' Defined Selenium Custom Methods to access into another class'''

class BasePage():

    def __init__(self,driver):
        self.driver = driver

    def get_element(self,by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))

    def click_element(self,by_locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator)).click()

    def send_keys(self,by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self,by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_element_present(self,by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element

    def get_title(self,title):
        WebDriverWait(self.driver, 100).until(EC.title_contains(title))
        return self.driver.title

