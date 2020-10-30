from .BaseSteps import *


class AuthForm(BaseSteps):
    LOGIN = '//input[@name="username"]'
    PASSWORD = '//input[@name="password"]'
    NEXT_BUTTON = '//button[@data-test-id="next-button"]'
    SUBMIT_BUTTON = '//button[@data-test-id="submit-button"]'

    def set_login(self, login):
        self.wait_until_and_get_elem_by_xpath(self.LOGIN).send_keys(login)

    def click_next(self):
        self.wait_until_and_get_elem_by_xpath(self.NEXT_BUTTON).click()

    def set_password(self, password):
        self.wait_until_and_get_elem_by_xpath(self.PASSWORD).send_keys(password)

    def submit(self):
        self.wait_until_and_get_elem_by_xpath(self.SUBMIT_BUTTON).click()

    def wait_for_cookie(self):
        self.wait_for_url('https://e.mail.ru/inbox/?afterReload=1')
