from steps.MainPageFoldersSteps import *
from .BasePage import *
from steps.MainPageFoldersSteps import MainPageFoldersSteps


class MainPageFolders(Page):
    BASE_URL = 'https://e.mail.ru/settings/folders'
    PATH = ''

    @property
    def pop3_steps(self):
        return MainPageFoldersSteps(self.driver)

    def click_change_checkbox_pop3(self) -> bool:
        """
                :return: True если checked, else False
        """
        classes_list = self.pop3_steps.toggle_checkbox_POP3()
        if len(classes_list.split()) == 2:
            return True
        return False

    def click_pencil_icon(self) -> bool:
        """
                :return: True если открылось окно
        """
        return self.pop3_steps.click_pencil_button()
