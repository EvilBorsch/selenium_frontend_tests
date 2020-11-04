from components.folders.add_folder_form import AddFolderForm
from .BasePage import *


class FoldersPage(Page):
    BASE_URL = 'https://e.mail.ru'
    PATH = '/settings/folders'

    @property
    def add_folder(self):
        return AddFolderForm(self.driver)
