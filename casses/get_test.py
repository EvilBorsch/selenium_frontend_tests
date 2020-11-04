# -*- coding: utf-8 -*-
import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote
from pages.AuthPage import AuthPage
from pages.MainPageFolders import MainPageFolders
from pages.UpdateFodlerPage import UpdateFolderPage
from pages.UpdatePasswordPage import UpdatePasswordPage

from enum import Enum
import random


class FoldersUpdateTest(unittest.TestCase):

    def runTest(self):
        """
        Тут описываются тест кейсы
        :return:
        """
        # Страница папок
        self.main_page_folders.open()

        self.test_toogle_checkbox()
        self.test_invalid_re_password()
        self.test_update_folder_name()
        self.test_select_top_folder()
        self.test_update_nested_folder()
        self.test_short_password()
        self.test_invalid_re_password()
        self.test_missing_secret_question()
        self.test_missing_secret_question_answer()
        self.test_valid_update_folder_form()

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
        self.main_page_folders = MainPageFolders(self.driver)
        self.update_folder = UpdateFolderPage(self.driver)
        self.update_password = UpdatePasswordPage(self.driver)
        self.__password_context = {
            'password': 'qwertyuiop',
            're_password': 'qwertyuiop',
            'question': 'why?',
            'question_answer': 'because',
            'current_password': os.environ['PASSWORD']
        }

    def go_to_main_folders(self):
        self.main_page_folders.open(self.main_page_folders.BASE_URL)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_toogle_checkbox(self):
        value_checkbox = self.main_page_folders.click_change_checkbox_pop3()
        value_checkbox2 = self.main_page_folders.click_change_checkbox_pop3()
        self.assertNotEqual(value_checkbox, value_checkbox2)
        self.go_to_main_folders()

    def test_update_folder_name(self):
        self.go_to_main_folders()
        ok = self.main_page_folders.click_pencil_icon()
        self.assertTrue(ok)
        is_filled = self.update_folder.fill_name("allahahbar")
        self.assertTrue(is_filled)
        self.update_folder.save_changes()

    def test_select_top_folder(self):
        self.go_to_main_folders()
        ok = self.main_page_folders.click_pencil_icon()
        self.assertTrue(ok)
        self.assertTrue(self.update_folder.fill_nested_folder('high_level'))
        ok = self.update_folder.save_changes()
        self.assertTrue(ok)

    def test_update_nested_folder(self):
        self.go_to_main_folders()
        ok = self.main_page_folders.click_pencil_icon()
        self.assertTrue(ok)

        class EnumForDropList(Enum):
            a = "incoming"
            b = "high_level"
            c = "drafts"

        self.update_folder.fill_nested_folder(random.choice(list(EnumForDropList)).value)
        ok = self.update_folder.save_changes()
        self.assertTrue(ok)

    def test_short_password(self):
        self.go_to_main_folders()
        ok = self.main_page_folders.click_pencil_icon()
        self.assertTrue(ok)
        self.update_folder.fill_checkbox({"password": True})
        self.update_folder.save_changes()
        context = self.__password_context.copy()
        context['password'] = 'ps'
        context['re_password'] = 'ps'
        self.update_password.set_password(context)
        self.assertTrue(self.update_password.get_password_form_errors['invalidPassword'])

    def test_invalid_re_password(self):
        self.go_to_main_folders()
        ok = self.main_page_folders.click_pencil_icon()
        self.assertTrue(ok)
        self.update_folder.fill_checkbox({"password": True})
        self.update_folder.save_changes()
        context = self.__password_context.copy()
        context['re_password'] = context['password'] + 'text'
        self.update_password.set_password(context)
        self.assertTrue(self.update_password.get_password_form_errors['invalidRePassword'])

    def test_missing_secret_question(self):
        self.go_to_main_folders()
        ok = self.main_page_folders.click_pencil_icon()
        self.assertTrue(ok)
        self.update_folder.fill_checkbox({"password": True})
        self.update_folder.save_changes()
        context = self.__password_context.copy()
        context['question'] = ''
        self.update_password.set_password(context)
        self.assertTrue(self.update_password.get_password_form_errors['invalidSecretQuestion'])

    def test_missing_secret_question_answer(self):
        self.go_to_main_folders()
        ok = self.main_page_folders.click_pencil_icon()
        self.assertTrue(ok)
        self.update_folder.fill_checkbox({"password": True})
        self.update_folder.save_changes()
        context = self.__password_context.copy()
        context['question_answer'] = ''
        self.update_password.set_password(context)
        self.assertTrue(self.update_password.get_password_form_errors['invalidSecretQuestionAnswer'])

    def test_invalid_current_password(self):
        self.go_to_main_folders()
        ok = self.main_page_folders.click_pencil_icon()
        self.assertTrue(ok)
        self.update_folder.fill_checkbox({"password": True})
        self.update_folder.save_changes()
        context = self.__password_context.copy()
        context['current_password'] = ''
        self.update_password.set_password(context)
        self.assertTrue(self.update_password.get_password_form_errors['invalidUserPassword'])

    def test_close_update_folder_form(self):
        self.go_to_main_folders()
        ok = self.main_page_folders.click_pencil_icon()
        self.assertTrue(ok)
        self.update_folder.fill_checkbox({"password": True})
        self.update_folder.save_changes()
        context = self.__password_context.copy()
        context['current_password'] = ''
        self.update_password.set_password(context)
        self.assertTrue(self.update_password.close())

    def test_cancel_update_folder_form(self):
        self.go_to_main_folders()
        ok = self.main_page_folders.click_pencil_icon()
        self.assertTrue(ok)
        self.update_folder.fill_checkbox({"password": True})
        self.update_folder.save_changes()
        context = self.__password_context.copy()
        context['current_password'] = ''
        self.update_password.set_password(context)
        self.assertTrue(self.update_password.back())
        self.assertTrue(self.update_password.back())

    def test_valid_update_folder_form(self):
        self.go_to_main_folders()
        ok = self.main_page_folders.click_pencil_icon()
        self.assertTrue(ok)
        self.update_folder.fill_checkbox({"password": True})
        self.update_folder.save_changes()
        context = self.__password_context.copy()
        self.update_password.set_password(context)
        ok = self.main_page_folders.click_pencil_icon()
        self.assertTrue(ok)
        self.update_folder.fill_checkbox({"password": False})
        self.update_password.update_password_steps.set_current_password(context['current_password'])
        self.update_password.update_password_steps.save()
