from selenium import webdriver
import pytest
from config.config import TestData

'''Defined which browser to be used for Testing'''

@pytest.fixture(params=["chrome", "firefox"], scope='class')
def init__driver(request):
    global web_driver
    if request.param == 'chrome':
        #web_driver = webdriver.Chrome(ChromeDriverManager().install())
        web_driver = webdriver.Chrome(executable_path=TestData.CHROME_BROWSER)
    if request.param == 'firefox':
         #web_driver = webdriver.Firefox(executable_path= GeckoDriverManager().install())
         web_driver = webdriver.Firefox(executable_path=TestData.FIREFOX_BROWSER)
    request.cls.driver = web_driver
    yield
    web_driver.close()
