# -*- coding: utf-8 -*-
import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from pages.AuthPage import AuthPage
from pages.MainPageFolders import MainPageFolders
from pages.UpdateFodlerPage import UpdateFolderPage
from pages.UpdatePasswordPage import UpdatePasswordPage
from pages.IdPage import Main_page
from pages.PersonalDataPage import Data_page
from enum import Enum
import random


class GetTest(unittest.TestCase):

    def runTest(self):
        """
        Тут описываются тест кейсы
        :return:
        """
        # Страница личных данных
        self.data_page.open(self.data_page.BASE_URL)
        self.test_fill_form_with_empty_name()
        self.test_fill_form_with_empty_city()

        # self.test_upload_avatar_by_btn()
        # self.test_upload_avatar_by_avatar()

        # Главная страница
        self.test_change_personal_info()
        print("Done 1")
        self.test_go_to_all_settings()
        print("Done 2")
        self.test_equality_names()
        print("Done 3")
        self.test_click_add_reserve_email()
        print("Done 4")
        print("Done main page tests")
        # Pop Up
        self.test_check_empty_email()
        print("Done 5")
        self.test_check_incorrect_email()
        print("Done 6")
        self.test_check_correct_email()
        print("Done 7")

        self.clear_email_after_tests()
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
        id_page = Main_page(self.driver)
        id_page.open(id_page.BASE_URL)
        self.data_page = Data_page(self.driver)
        self.main_page = Main_page(self.driver)
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

    def go_to_main(self):
        self.main_page.open(self.main_page.BASE_URL)

    def clear_email_after_tests(self):
        self.main_page.clear_reserve_email()

    def go_to_main_folders(self):
        self.main_page_folders.open(self.main_page_folders.BASE_URL)

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

    def test_click_add_reserve_email(self):
        ok = self.main_page.click_add_reserve_email()
        self.assertTrue(ok)

    def test_check_empty_email(self):
        res = self.main_page.add_email("")
        self.assertEqual(res, "Укажите почту")

    def test_check_incorrect_email(self):
        res = self.main_page.add_email("asd")
        self.assertEqual(res, "Неправильная почта. Укажите другую.")

    def test_check_correct_email(self):
        header = self.main_page.add_email("correct@yandex.ru")
        self.assertEqual(header, "Резервная почта добавлена")

    # def test_upload_avatar_by_btn(self):
    #     test_path = os.path.abspath("../avatar.jpg")
    #     self.data_page.change_avatar_by_button(test_path)

    def test_upload_avatar_by_avatar(self):
        test_path = os.path.abspath("../avatar.jpg")
        self.data_page.change_avatar_by_avatar(test_path)

    def test_fill_form_with_empty_city(self):
        errors = self.data_page.fill_form("Имя", "Фамилия", "Никнейм", "")
        self.assertEqual(errors.city_err, "Укажите город")
        self.assertEqual(errors.name_err, "")
        self.assertEqual(errors.last_name_err, "")
        self.assertEqual(errors.nickname_err, "")

    def test_fill_form_with_empty_name(self):
        errors = self.data_page.fill_form("", "Фамилия", "Никнейм", "Москва, Россия")
        self.assertEqual(errors.city_err, "")
        self.assertEqual(errors.name_err, "Укажите имя")
        self.assertEqual(errors.last_name_err, "")
        self.assertEqual(errors.nickname_err, "")

    def test_fill_with_wrong_city(self):
        errors = self.data_page.fill_form("Имя", "Фамилия", "Никнейм", "")
        self.assertEqual(errors.city_err, "Укажите город")
        self.assertEqual(errors.name_err, "")
        self.assertEqual(errors.last_name_err, "")
        self.assertEqual(errors.nickname_err, "")

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
