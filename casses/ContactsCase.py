import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote
from pages.SecurityPage import SecurityPage
from cases.BaseCase import Test
from pages.ContactsPage import ContactsPage
import time

class ContactsTest(Test):
    
    def setUp(self):
        super().setUp()

        contacts_page = ContactsPage(self.driver)
        contacts_page.open()
        self.page = ContactsPage(self.driver)

    def test_add_email_button(self):
        self.page.open_add_email_popup()
        self.assertTrue(self.page.is_add_email_popup_open())

    def test_add_phone_button(self):
        self.page.open_add_phone_popup()
        self.assertTrue(self.page.is_add_phone_popup_open())

    def test_delete_email(self):
        self.page.open_add_email_popup()
        self.page.add_backup_email('test_login_a.elagin1@mail.ru')
        
        self.go_to_main()
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
        
