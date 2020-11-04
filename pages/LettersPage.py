from components.letters.header import LettersHeader
from .BasePage import *


class LettersPage(Page):
    BASE_URL = 'https://e.mail.ru'
    PATH = ''

    @property
    def header(self):
        return LettersHeader(self.driver)
