# -*- coding: utf-8 -*-
import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from pages.AuthPage import AuthPage
from pages.MainPage import Main_page
from pages.UpdateFodlerPage import UpdateFolderPage
from enum import Enum
import random


class GetTest(unittest.TestCase):

    def runTest(self):
        """
        Тут описываются тест кейсы
        :return:
        """
        # Страница папок
        self.main_page.open()
        # self.test_toogle_checkbox()
        self.test_update_folder()

        # self.test_upload_avatar_by_btn()
        # self.test_upload_avatar_by_avatar()



        self.clear_email_after_tests()
        print("Done Pop Up tests")

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
        id_page.open(id_page.BASE_URL)
        self.main_page = Main_page(self.driver)
        self.update_folder = UpdateFolderPage(self.driver)

    def go_to_main(self):
        self.main_page.open(self.main_page.BASE_URL)

    def clear_email_after_tests(self):
        pass

    def tearDown(self) -> None:
        self.driver.quit()

    def test_toogle_checkbox(self):
        value_checkbox = self.main_page.click_change_checkbox_pop3()
        value_checkbox2 = self.main_page.click_change_checkbox_pop3()
        self.assertNotEqual(value_checkbox, value_checkbox2)
        self.go_to_main()

    def test_update_folder(self):
        self.go_to_main()
        ok = self.main_page.click_pencil_icon()
        self.assertTrue(ok)
        is_filled = self.update_folder.fill_name("allahahbar")
        self.assertTrue(is_filled)

        class EnumForDropList(Enum):
            a = "incoming"
            b = "high_level"
            c = "drafts"

        self.update_folder.fill_nested_folder("high_level")
        self.assertTrue(random.choice(list(EnumForDropList)).value)
