import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote

from steps.account import AccountSteps
from steps.folders import FoldersSteps


class LoginTest(unittest.TestCase):

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.accountSteps = AccountSteps(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        self.accountSteps.login(os.environ['LOGIN'], os.environ['PASSWORD'])
        self.assertTrue(self.accountSteps.email == os.environ['LOGIN'])


class FoldersTest(unittest.TestCase):

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        self.accountSteps = AccountSteps(self.driver)
        self.folderSteps = FoldersSteps(self.driver)
        self.accountSteps.login(os.environ['LOGIN'], os.environ['PASSWORD'])

        self.__password_context = {
            'password': 'qwertyuiop',
            're_password': 'qwertyuiop',
            'question': 'why?',
            'question_answer': 'because',
            'current_password': os.environ['PASSWORD']
        }

    def tearDown(self):
        self.driver.quit()

    def test_empty_folder_name(self):
        self.folderSteps.add_folder('')
        self.assertTrue(self.folderSteps.get_form_errors()['emptyFolderName'])    #OK

    def test_spaces_folder_name(self):
        self.folderSteps.add_folder('     ')
        self.assertTrue(self.folderSteps.get_form_errors()['emptyFolderName'])    #OK

    def test_select_top_folder(self):
        self.folderSteps.add_folder('folder1', 'Папка на верхнем уровне')         #OK
        self.folderSteps.delete_folder()

    def test_select_check_incoming_folder(self):
        self.folderSteps.add_folder('folder2', 'Входящие')                        #OK
        self.folderSteps.delete_folder()

    def test_select_check_sent_folder(self):
        self.folderSteps.add_folder('folder3', 'Отправленные')                    #OK
        self.folderSteps.delete_folder()

    def test_select_drafts(self):
        self.folderSteps.add_folder('folder4', 'Черновики')                       #OK
        self.folderSteps.delete_folder()

    def test_pop3_check_box(self):
        self.folderSteps.add_folder('folder5', '', ['pop3'])                      #OK
        self.folderSteps.delete_folder()

    def test_archive_check_box(self):
        self.folderSteps.add_folder('folder6', '', ['archive'])                   #OK
        self.folderSteps.delete_folder()

    def test_folder_with_password(self):
        context = self.__password_context.copy()
        self.folderSteps.add_folder('folder7', '', ['has password'], context)
        self.folderSteps.delete_folder()                                          #OK

    def test_short_password(self):
        context = self.__password_context.copy()
        context['password'] = 'ps'
        context['re_password'] = 'ps'
        self.folderSteps.add_folder('folder7', '', ['has password'], context)
        self.assertTrue(self.folderSteps.get_form_errors()['passwordForm']['invalidPassword'])    #OK

    def test_long_password(self):
        context = self.__password_context.copy()
        context['password'] = 'ps' * 32
        context['re_password'] = 'ps' * 32
        self.folderSteps.add_folder('folder7', '', ['has password'], context)
        self.assertTrue(self.folderSteps.get_form_errors()['passwordForm']['invalidPassword'])  #OK

    def test_password_started_with_space(self):
        context = self.__password_context.copy()
        context['password'] = ' ' + context['password']
        context['re_password'] = ' ' + context['password']
        self.folderSteps.add_folder('folder7', '', ['has password'], context)
        self.assertTrue(self.folderSteps.get_form_errors()['passwordForm']['invalidPassword'])   #OK

    def test_password_ended_with_space(self):
        context = self.__password_context.copy()
        context['password'] = context['password'] + ' '
        context['re_password'] = context['password'] + ' '
        self.folderSteps.add_folder('folder7', '', ['has password'], context)
        self.assertTrue(self.folderSteps.get_form_errors()['passwordForm']['invalidPassword'])      #OK

    def test_invalid_password(self):
        context = self.__password_context.copy()
        context['password'] = '@#$%^&*()askdl'
        context['re_password'] = context['password']
        self.folderSteps.add_folder('folder7', '', ['has password'], context)
        self.assertTrue(self.folderSteps.get_form_errors()['passwordForm']['invalidPassword'])      #OK

    def test_invalid_re_password(self):
        context = self.__password_context.copy()
        context['re_password'] = context['password'] + 'text'
        self.folderSteps.add_folder('folder7', '', ['has password'], context)
        self.assertTrue(self.folderSteps.get_form_errors()['passwordForm']['invalidRePassword'])        #OK

    def test_missing_secret_question(self):
        context = self.__password_context.copy()
        context['question'] = ''
        self.folderSteps.add_folder('folder7', '', ['has password'], context)
        self.assertTrue(self.folderSteps.get_form_errors()['passwordForm']['invalidSecretQuestion'])    #OK

    def test_missing_secret_question_answer(self):
        context = self.__password_context.copy()
        context['question_answer'] = ''
        self.folderSteps.add_folder('folder7', '', ['has password'], context)
        self.assertTrue(self.folderSteps.get_form_errors()['passwordForm']['invalidSecretQuestionAnswer'])  #OK

    def test_invalid_current_password(self):
        context = self.__password_context.copy()
        context['current_password'] = ''
        self.folderSteps.add_folder('folder7', '', ['has password'], context)
        self.assertTrue(self.folderSteps.get_form_errors()['passwordForm']['invalidUserPassword'])  #OK

    def test_close_add_folder_form(self):
        self.folderSteps.folders_page.open()
        self.folderSteps.folders_page.add_folder.open()
        self.folderSteps.folders_page.add_folder.close()                                              #OK

    def test_cancel_add_folder_form(self):
        self.folderSteps.folders_page.open()
        self.folderSteps.folders_page.add_folder.open()
        self.folderSteps.folders_page.add_folder.cancel()                                               #OK
