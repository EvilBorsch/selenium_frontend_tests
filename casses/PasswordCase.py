import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote
from pages.SecurityPage import SecurityPage
from cases.BaseCase import Test
from pages.PasswordPopup import PasswordPopup


class PasswordTest(Test):

    def setUp(self):
        super().setUp()

        password_page = PasswordPopup(self.driver)
        password_page.open()
        self.page = PasswordPopup(self.driver)
        
    def test_send_empty_form(self):
        self.page.send_empty_form()
        self.assertTrue(
            self.page.is_new_password_error() 
            and self.page.is_current_password_error() 
            and self.page.is_repeat_password_error()
            )


    def test_change_password(self):
        NEW_PASSWORD = '12893490278kek'

        self.page.change_password(self.password, NEW_PASSWORD)
        changed = self.page.is_password_changed()
        self.page.open()

        self.page.change_password(NEW_PASSWORD, self.password)
        changed_again = self.page.is_password_changed()
        self.assertTrue(changed and changed_again)

    def test_change_password_with_invalid_repeat_password(self):
        NEW_PASSWORD = '12893490278kek'

        self.page.send_form_with_uncorrect_repeat(NEW_PASSWORD, self.password)
        self.assertTrue(self.page.is_new_password_error() and self.page.is_repeat_password_error())

    def test_generate_password(self):
        self.page.generate_password()
        self.assertTrue(self.page.get_new_password_security() == "Надёжный пароль")

        self.assertEqual(self.page.get_repeat_password_value(), self.page.get_new_password_value())


    def test_long_new_password(self):
        text = self.page.set_new_password_and_get_password_security_value("12345678aB12345678aB12345678aB12345678aB1")
        self.assertEqual(text, 'Пароль слишком длинный')

    def test_numeric_new_password(self):
        text = self.page.set_new_password_and_get_password_security_value("1234567890")
        self.assertEqual(text, 'Ненадёжный пароль')

    def test_small_new_password(self):
        text = self.page.set_new_password_and_get_password_security_value("aa12A")
        self.assertEqual(text, 'Ненадёжный пароль')

    def test_close_popup(self):

        self.page.close_popup()
        self.assertFalse(self.page.is_popup_open())

    def test_cancel_popup(self):

        self.page.cancel()
        self.assertFalse(self.page.is_popup_open())

    def test_password_visibity(self):
        self.page.change_fields(self.password, "PASSW0RdD")

        self.page.change_new_password_visibility()
        self.page.change_old_password_visibility()

        isOkey = self.page.is_new_password_visible() and self.page.is_old_password_visibile()

        self.page.change_new_password_visibility()
        self.page.change_old_password_visibility()

        self.assertTrue(not (self.page.is_new_password_visible() or self.page.is_old_password_visibile()) and isOkey)

