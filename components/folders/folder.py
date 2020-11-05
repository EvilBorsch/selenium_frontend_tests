from components.base import BaseComponent
from selenium.webdriver.support.ui import WebDriverWait


class Folder(BaseComponent):
    DELETE_FOLDER = '//button[@data-test-id="folder-delete"]'
    APPLY_BUTTON = '//button[@data-test-id="submit"]'
    PASSWORD_INPUT = '//input[@data-test-id="folderPassword"]'
    FORM_CONTAINER = '//div[@data-test-id="cross"]'

    def delete_folder(self, folder_name):
        folder_xpath = '//div[@data-test-id="folder:{}"]'.format(folder_name)
        self.wait_until_and_get_elem_by_xpath(folder_xpath + self.DELETE_FOLDER).click()

    def apply(self):
        self.wait_until_and_get_elem_by_xpath(self.APPLY_BUTTON).click()

    def input_password(self, password):
        self.wait_until_and_get_elem_by_xpath(self.PASSWORD_INPUT).send_keys(password)

    def wait_folder(self, folder_name):
        folder_xpath = '//div[@data-test-id="folder:{}"]'.format(folder_name)
        self.wait_until_and_get_elem_by_xpath(folder_xpath + self.DELETE_FOLDER)

    def wait_form(self):
        self.wait_until_and_get_elem_by_xpath(self.FORM_CONTAINER)

    @property
    def input(self):
        return len(self.driver.find_elements_by_xpath(self.PASSWORD_INPUT)) != 0
