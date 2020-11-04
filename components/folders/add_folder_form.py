from components.base import BaseComponent
from components.folders.folder import Folder
from components.folders.attachment_select import AttachmentSelect
from components.folders.password_from import PasswordForm


class AddFolderForm(BaseComponent):
    ADD_FOLDER_BUTTON = '//button[@data-test-id="create"]'
    FOLDER_NAME_INPUT = '//input[@data-test-id="name"]'
    POP3_CHECKBOX = '//label[@data-test-id="pop3"]'
    ARCHIVE_CHECKBOX = '//label[@data-test-id="makeArchive"]'
    HAS_PASSWORD_CHECKBOX = '//label[@data-test-id="hasPassword"]'
    CREATE_FOLDER_BUTTON = '//button[@data-test-id="submit"]'
    CANCEL_CREATE_FOLDER_BUTTON = '//button[@data-test-id="cancel"]'
    CLOSE_CREATE_FOLDER_BUTTON = '//div[@data-test-id="cross"]'
    EMPTY_FOLDER_NAME_ERROR = '//span[@data-test-id="emptyFolderName"]'

    @property
    def select(self):
        return AttachmentSelect(self.driver)

    @property
    def password(self):
        return PasswordForm(self.driver)

    @property
    def folder(self):
        return Folder(self.driver)

    def open(self):
        self.wait_until_and_get_elem_by_xpath(self.ADD_FOLDER_BUTTON).click()

    def set_folder_name(self, name):
        self.wait_until_and_get_elem_by_xpath(self.FOLDER_NAME_INPUT).send_keys(name)

    def set_pop3(self):
        self.wait_until_and_get_elem_by_xpath(self.POP3_CHECKBOX).click()

    def set_archive(self):
        self.wait_until_and_get_elem_by_xpath(self.ARCHIVE_CHECKBOX).click()

    def set_has_password(self):
        self.wait_until_and_get_elem_by_xpath(self.HAS_PASSWORD_CHECKBOX).click()

    def add(self):
        self.wait_until_and_get_elem_by_xpath(self.CREATE_FOLDER_BUTTON).click()

    def cancel(self):
        self.wait_until_and_get_elem_by_xpath(self.CANCEL_CREATE_FOLDER_BUTTON).click()

    def close(self):
        self.wait_until_and_get_elem_by_xpath(self.CLOSE_CREATE_FOLDER_BUTTON).click()

    @property
    def empty_folder_name_error(self):
        return len(self.driver.find_elements_by_xpath(self.CANCEL_CREATE_FOLDER_BUTTON)) != 0

    @property
    def get_password_form_errors(self):
        return {'invalidPassword': self.password.invalid_password_error,
                'invalidRePassword': self.password.invalid_re_password_error,
                'invalidSecretQuestion': self.password.invalid_secret_question_error,
                'invalidSecretQuestionAnswer': self.password.invalid_secret_question_answer_error,
                'invalidUserPassword': self.password.invalid_user_password_error}