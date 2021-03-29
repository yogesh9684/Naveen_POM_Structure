from Test.test_base import BaseTest
from Pages.Login_Page import LoginPage
from config.config import TestData


'''Test Cases for the Login Page'''

class Test_Login(BaseTest):

    def test_title_of_page(self):
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_title(TestData.PAGE_TITLE)
        assert title == TestData.PAGE_TITLE

    def test_login_functionality(self):
            self.loginPage = LoginPage(self.driver)
            self.loginPage.make_login(TestData.EMAIL , TestData.PASSWORD)



