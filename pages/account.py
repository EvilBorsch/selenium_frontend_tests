from pages.base import BasePage
from components.account.login_form import LoginForm
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class LoginPage(BasePage):
    BASE_URL = 'https://account.mail.ru'
    PATH = ''

    @property
    def form(self):
        return LoginForm(self.driver)

    def wait_for_login(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.url_to_be('https://e.mail.ru/inbox/?afterReload=1')
        )
