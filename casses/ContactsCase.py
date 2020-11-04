import os
import unittest

from selenium.webdriver import DesiredCapabilities

from pages.AuthPage import AuthPage, Remote
from pages.ContactsPage import ContactsPage


class ContactsTest(unittest.TestCase):
    def setUp(self) -> None:
        browser = os.environ.get('BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        LOGIN = os.environ['LOGIN']
        PASSWORD = os.environ['PASSWORD']
        self.password = PASSWORD
        self.login = LOGIN

        auth_page = AuthPage(self.driver)
        auth_page.auth(LOGIN, PASSWORD)
        contacts_page = ContactsPage(self.driver)
        contacts_page.open()
        self.page = ContactsPage(self.driver)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_add_email_button(self):
        self.page.open_add_email_popup()
        self.assertTrue(self.page.is_add_email_popup_open())

    def test_add_phone_button(self):
        self.page.open_add_phone_popup()
        self.assertTrue(self.page.is_add_phone_popup_open())

    def test_delete_email(self):
        self.page.open_add_email_popup()
        self.page.add_backup_email('test_login_a.elagin1@mail.ru')

        self.page.open()
        self.page.delete_email()

        self.assertTrue(self.page.has_not_backup_email())

    def test_invalid_phone(self):
        self.page.open_add_phone_popup()

        self.page.send_phone('1231')

        self.assertEqual(self.page.get_phone_error(), 'Неправильный номер. Укажите другой.')

    def test_close_phone_popup(self):
        self.page.open_add_phone_popup()
        self.page.close_phone_popup()
        self.assertTrue(self.page.is_add_phone_popup_close())

    def test_cancel_phone_popup(self):
        self.page.open_add_phone_popup()
        self.page.cancle_phone_popup()
        self.assertTrue(self.page.is_add_phone_popup_close())
