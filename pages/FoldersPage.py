from components.folders.add_folder_form import AddFolderForm
from steps.MainPageFoldersSteps import MainPageFoldersSteps
from .BasePage import *


class FoldersPage(Page):
    BASE_URL = 'https://e.mail.ru'
    PATH = '/settings/folders'

    @property
    def add_folder(self):
        return AddFolderForm(self.driver)

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
