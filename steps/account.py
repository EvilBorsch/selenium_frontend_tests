from steps.base import BaseStep
from pages.account import LoginPage
from pages.letters import LettersPage


class AccountSteps(BaseStep):

    def __init__(self, driver):
        super(AccountSteps, self).__init__(driver)
        self.login_page = LoginPage(driver)
        self.letter_page = LettersPage(driver)

    def login(self, username, password):
        self.login_page.open()
        self.login_page.form.set_login(username)
        self.login_page.form.next()
        self.login_page.form.set_password(password)
        self.login_page.form.submit()
        self.login_page.wait_for_login()

    @property
    def email(self):
        return self.letter_page.header.email
