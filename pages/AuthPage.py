from steps.authSteps import *
from .BasePage import *


class AuthPage(Page):
    BASE_URL = 'https://account.mail.ru'
    PATH = ''

    @property
    def login_form(self):
        return AuthForm(self.driver)

    def auth(self, login, password):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_page.login_form.set_login(login)
        auth_page.login_form.click_next()
        auth_page.login_form.set_password(password)
        auth_page.login_form.submit()
        auth_page.login_form.wait_for_cookie()
