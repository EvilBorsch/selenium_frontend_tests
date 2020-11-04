import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote
from pages.AuthPage import AuthPage
from pages.SecurityPage import SecurityPage



class Test(unittest.TestCase):
    page = None

    def setUp(self):
        browser = 'CHROME'
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        LOGIN = os.environ['LOGIN']
        PASSWORD = os.environ['PASSWORD']
        self.password = PASSWORD
        self.login = LOGIN

        self.auth(self.password)

    def auth(self, password):
        auth_page = AuthPage(self.driver)
        auth_page.auth(self.login, password)


    def go_to_main(self):
        self.page.open(self.page.BASE_URL)
        

    def tearDown(self):
        self.driver.quit()