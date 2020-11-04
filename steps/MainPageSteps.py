from selenium.common.exceptions import TimeoutException

from .BaseSteps import *


class MainPageSteps(BaseSteps):
    pop3_checkbox_path = '(//label[@data-test-id="folder-pop3"])[1]'
    pop3_checkbox_div_path = '((//label[@data-test-id="folder-pop3"])[1])/div'
    update_folder_path = '((((//button[@data-test-id="folder-delete"]))/..)/..)//button[@data-test-id="folder-edit"]'
    modal_header_path = '//div[@class="c01505"]'

    def toggle_checkbox_POP3(self) -> str:
        """
        :return: Классы div для чекбокса
        """
        self.wait_until_and_get_elem_by_xpath(self.pop3_checkbox_path).click()

        return self.wait_until_and_get_elem_by_xpath(self.pop3_checkbox_div_path).get_attribute('class')

    def click_pencil_button(self) -> bool:
        """
                :return: True если открылось модальное окно
        """
        try:
            self.wait_until_and_get_elem_by_xpath(self.update_folder_path).click()
            return True
        except TimeoutException:
            return False
