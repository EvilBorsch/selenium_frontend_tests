from pages.base import BasePage
from components.folders.add_folder_form import AddFolderForm


class FoldersPage(BasePage):
    BASE_URL = 'https://e.mail.ru'
    PATH = '/settings/folders'

    @property
    def add_folder(self):
        return AddFolderForm(self.driver)
