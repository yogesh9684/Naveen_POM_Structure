from Pages.Login_Page import LoginPage
from Test.test_base import BaseTest
from config.config import TestData
import time


class Test_HomePage(BaseTest):

    # def test_home_page_title(self):
    #     self.loginPage = LoginPage(self.driver)
    #     homePage = self.loginPage.make_login(TestData.EMAIL,TestData.PASSWORD)
    #     title = homePage.verify_home_page_title(TestData.HOME_PAGE_TITLE)
    #     assert title == TestData.HOME_PAGE_TITLE


    def test_send_values_on_search(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.make_login(TestData.EMAIL, TestData.PASSWORD)
        homePage.send_text_on_search(TestData.SEARCH_TEXT)
        homePage.click_on_Moxie_Logo()
        homePage.click_on_classes()




