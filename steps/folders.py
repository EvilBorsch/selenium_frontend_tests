from steps.base import BaseStep
from pages.folders import FoldersPage
from time import sleep


class FoldersSteps(BaseStep):

    def __init__(self, driver):
        super(FoldersSteps, self).__init__(driver)
        self.folders_page = FoldersPage(driver)

    def add_folder(self, name, option="", boxes=(), password_context={}):
        self.folders_page.open()
        self.folders_page.add_folder.open()
        self.folders_page.add_folder.set_folder_name(name)
        self.select_folder_option(option)
        self.set_checkboxes(boxes)
        self.folders_page.add_folder.add()
        if password_context:
            self.set_password(password_context)

    def wait_folder(self, name):
        self.folders_page.add_folder.folder.wait_folder(name)

    def select_folder_option(self, option):
        if option:
            self.folders_page.add_folder.select.open()
        if option == "Папка на верхнем уровне":
            self.folders_page.add_folder.select.select_folder_top()
        elif option == "Входящие":
            self.folders_page.add_folder.select.select_incoming()
        elif option == "Отправленные":
            self.folders_page.add_folder.select.select_sent()
        elif option == "Черновики":
            self.folders_page.add_folder.select.select_drafts()

    def set_checkboxes(self, boxes):
        if 'pop3' in boxes:
            self.folders_page.add_folder.set_pop3()
        if 'archive' in boxes:
            self.folders_page.add_folder.set_archive()
        if 'has password' in boxes:
            self.folders_page.add_folder.set_has_password()

    def set_password(self, password_context):
        self.folders_page.add_folder.password.set_password(password_context['password'])
        self.folders_page.add_folder.password.set_re_password(password_context['re_password'])
        self.folders_page.add_folder.password.set_question(password_context['question'])
        self.folders_page.add_folder.password.set_question_answer(password_context['question_answer'])
        self.folders_page.add_folder.password.set_current_password(password_context['current_password'])
        self.folders_page.add_folder.password.save()

    def delete_folder(self, name, password=""):
        self.folders_page.open()
        self.folders_page.add_folder.folder.delete_folder(name)
        if self.folders_page.add_folder.folder.input:
            self.folders_page.add_folder.folder.input_password(password)
            self.folders_page.add_folder.folder.apply()
            self.folders_page.add_folder.folder.wait_form()

        self.folders_page.add_folder.folder.apply()
        sleep(10)

    def get_form_errors(self):
        return {'emptyFolderName': self.folders_page.add_folder.empty_folder_name_error,
                'passwordForm': self.folders_page.add_folder.get_password_form_errors}

