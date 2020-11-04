import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote
from pages.SecurityPage import SecurityPage
from cases.BaseCase import Test


class SecurityTest(Test):

    def runTest(self):
        self.test_click_history_link()
        self.test_click_oauth_link()
        self.test_click_devices_link()
        self.test_click_services_link()
        self.test_click_setPassword_link()
        self.test_click_keys_link()
        self.test_click_password_more_link()
        self.test_click_keys_more_link()
        self.test_click_twofact_more_link()

    def setUp(self):
        super().setUp()
        security_page = SecurityPage(self.driver)
        security_page.open()
        self.page = SecurityPage(self.driver)

    def test_click_devices_link(self):
        isOkey = self.page.click_devices_link()
        self.assertTrue(isOkey)

    def test_click_services_link(self):
        isOkey = self.page.click_services_link()
        self.assertTrue(isOkey)

    def test_click_setPassword_link(self):
        isOkey = self.page.click_setPassword_link()
        self.assertTrue(isOkey)

    def test_click_history_link(self):
        isOkey = self.page.click_history_link()
        self.assertTrue(isOkey)

    def test_click_oauth_link(self):
        isOkey = self.page.click_oauth_link()
        self.assertTrue(isOkey)

    def test_click_keys_link(self):
        isOkey = self.page.click_keys_link()
        self.assertTrue(isOkey)

    def test_click_twofact_more_link(self):
        isOkey = self.page.click_twofact_more_link()
        self.assertTrue(isOkey)
    
    def test_click_keys_more_link(self):
        isOkey = self.page.click_keys_more_link()
        self.assertTrue(isOkey)

        
    