from components.base import BaseComponent
from selenium.webdriver.support.ui import WebDriverWait


class Folder(BaseComponent):
    DELETE_FOLDER = '//button[@data-test-id="folder-delete"]'
    APPLY_BUTTON = '//button[@data-test-id="submit"]'

    def delete(self):
        self.wait_until_and_get_elem_by_xpath(self.DELETE_FOLDER).click()

    def apply(self):
        self.wait_until_and_get_elem_by_xpath(self.APPLY_BUTTON).click()
