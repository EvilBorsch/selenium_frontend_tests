import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from pages.AuthPage import AuthPage
from pages.IdPage import Main_page


class GetTest(unittest.TestCase):
    def runTest(self):
        """
        Тут описываются тест кейсы
        :return:
        """
        self.test_change_personal_info()
        self.test_go_to_all_settings()
        self.test_equality_names()


    def setUp(self) -> None:
        browser = 'CHROME'
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        LOGIN = os.environ['LOGIN']
        PASSWORD = os.environ['PASSWORD']

        auth_page = AuthPage(self.driver)
        auth_page.auth(LOGIN, PASSWORD)
        id_page = Main_page(self.driver)
        id_page.open()
        self.main_page = Main_page(self.driver)

    def go_to_main(self):
        self.main_page.open(self.main_page.BASE_URL)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_change_personal_info(self):
        ok = self.main_page.click_change_personal_info()
        self.assertTrue(ok)
        self.go_to_main()

    def test_go_to_all_settings(self):
        ok = self.main_page.click_get_all_settings()
        self.assertTrue(ok)
        self.go_to_main()

    def test_equality_names(self):
        self.assertEqual(self.main_page.get_name_surname_from_left_bar(), self.main_page.get_name_surname_from_card())

