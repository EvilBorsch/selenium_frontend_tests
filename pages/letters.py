from pages.base import BasePage
from components.letters.header import LettersHeader


class LettersPage(BasePage):
    BASE_URL = 'https://e.mail.ru'
    PATH = ''

    @property
    def header(self):
        return LettersHeader(self.driver)
