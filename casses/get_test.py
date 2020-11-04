# -*- coding: utf-8 -*-
import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from pages.AuthPage import AuthPage
from pages.MainPage import Main_page
from pages.UpdateFodlerPage import UpdateFolderPage
from pages.UpdatePasswordPage import UpdatePasswordPage

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
        self.test_short_password()

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
        self.update_password = UpdatePasswordPage(self.driver)
        self.__password_context = {
            'password': 'qwertyuiop',
            're_password': 'qwertyuiop',
            'question': 'why?',
            'question_answer': 'because',
            'current_password': os.environ['PASSWORD']
        }

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

    def test_update_folder_name(self):
        self.go_to_main()
        ok = self.main_page.click_pencil_icon()
        self.assertTrue(ok)
        is_filled = self.update_folder.fill_name("allahahbar")
        self.assertTrue(is_filled)
        self.update_folder.save_changes()

    def test_select_top_folder(self):
        self.go_to_main()
        self.assertTrue(self.update_folder.fill_nested_folder('high_level'))
        ok = self.update_folder.save_changes()
        self.assertTrue(ok)

    def test_update_nested_folder(self):
        self.go_to_main()

        class EnumForDropList(Enum):
            a = "incoming"
            b = "high_level"
            c = "drafts"

        self.update_folder.fill_nested_folder(random.choice(list(EnumForDropList)).value)
        ok = self.update_folder.save_changes()
        self.assertTrue(ok)

    def test_short_password(self):
        self.go_to_main()
        ok = self.main_page.click_pencil_icon()
        self.assertTrue(ok)
        self.update_folder.fill_checkbox({"password": True})
        self.update_folder.save_changes()
        context = self.__password_context.copy()
        context['password'] = 'ps'
        context['re_password'] = 'ps'
        self.update_password.set_password(context)
        self.assertTrue(self.update_password.get_password_form_errors['invalidPassword'])
