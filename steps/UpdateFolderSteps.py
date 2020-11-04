from .BaseSteps import *
from selenium.common.exceptions import TimeoutException


class UpdateFolderSteps(BaseSteps):
    update_folder_path = '//*[@id="root"]/div/div[3]/div/div[6]/div[6]/span[6]/button'
    modal_header_path = '//div[@class="c01505"]'
    checkbox_pop3_path = '//label[@data-test-id="pop3"]'
    checkbox_archive_path = '//label[@data-test-id="makeArchive"]'
    checkbox_password_path = '//label[@data-test-id="hasPassword"]'
    save_button_path = '//button[@data-test-id="submit"]'
    cross_path = '//div[@data-test-id="cross"]'
    cancel_button_path = '//button[@data-test-id="cancel"]'
    input_name_path = '//input[@data-test-id="name"]'

    OPEN_BUTTON = '//span[@data-test-id="createFolder-select-value"]'
    FOLDER_TOP_SELECT = '//div[@data-test-id="select-value:-1"]'
    INCOMING_SELECT = '//div[@data-test-id="select-value:0"]'
    SENT_SELECT = '//div[@data-test-id="select-value:500000"]'
    DRAFTS_SELECT = '//div[@data-test-id="select-value:500001"]'
    SELECT = ' data-test-id="createFolder-select-value"'

    def toggle_checkbox_pop3(self) -> bool:
        """
                :return: True if checked, false if not checked
        """
        checkbox = self.wait_until_and_get_elem_by_xpath(self.checkbox_pop3_path)
        checkbox.click()
        return checkbox.is_selected()

    def toggle_checkbox_make_archive(self) -> bool:
        """
                :return: True if checked, false if not checked
        """
        self.wait_until_and_get_elem_by_xpath(self.checkbox_archive_path).click()
        checkbox_classes: str = self. \
            wait_until_and_get_elem_by_xpath(self.checkbox_archive_path) \
            .get_attribute('class')

        return len(checkbox_classes.split()) == 2 or False

    def toggle_checkbox_password(self) -> bool:
        """
                :return: True if checked, false if not checked
        """
        self.wait_until_and_get_elem_by_xpath(self.checkbox_password_path).click()
        checkbox_classes: str = self. \
            wait_until_and_get_elem_by_xpath(self.checkbox_password_path) \
            .get_attribute('class')

        return len(checkbox_classes.split()) == 2 or False

    def set_value_of_drop_list(self, value: str) -> bool:
        """
                :return: Вернет True если пункт переключился
        """
        self.open()
        if value == "incoming":
            return self.select_incoming()
        elif value == "high_level":
            return self.select_folder_top()
        elif value == "drafts":
            return self.select_drafts()
        else:
            return self.select_sent()

    def set_input_name(self, value: str) -> str:
        """
                :return: Вернет слово из input
        """
        selected_item = self.wait_until_and_get_elem_by_xpath(self.input_name_path)
        self.fill_input(self.input_name_path, value)

        # self.driver.execute_script(f"arguments[0].setAttribute('value','{value}')", selected_item)
        return selected_item.get_attribute("value")

    def click_save_button(self) -> str:
        """
                :return: Текст в хедере модального окна
        """
        self.wait_until_and_get_elem_by_xpath(self.save_button_path).click()
        header_text: str = ""
        try:
            header_text = self.wait_until_and_get_elem_by_xpath(self.modal_header_path).text
            return header_text
        except TimeoutException:
            header_text = ""
        finally:
            return header_text

    def click_cross_button(self) -> str:
        """
                :return: Текст в хедере модального окна
        """
        self.wait_until_and_get_elem_by_xpath(self.cross_path).click()
        return self.wait_until_and_get_elem_by_xpath(self.modal_header_path).text

    def click_cancel_button(self) -> str:
        """
                :return: Текст в хедере модального окна
        """
        self.wait_until_and_get_elem_by_xpath(self.cancel_button_path).click()
        return self.wait_until_and_get_elem_by_xpath(self.modal_header_path).text

    def open(self):
        try:
            self.wait_until_and_get_elem_by_xpath(self.OPEN_BUTTON).click()
            return True
        except TimeoutException:
            return False

    def select_folder_top(self):
        try:
            self.wait_until_and_get_elem_by_xpath(self.FOLDER_TOP_SELECT).click()
            return True
        except TimeoutException:
            return False

    def select_incoming(self):
        try:
            self.wait_until_and_get_elem_by_xpath(self.INCOMING_SELECT).click()
            return True
        except TimeoutException:
            return False

    def select_sent(self) -> bool:
        try:
            self.wait_until_and_get_elem_by_xpath(self.SENT_SELECT).click()
            return True
        except TimeoutException:
            return False

    def select_drafts(self):
        try:
            self.wait_until_and_get_elem_by_xpath(self.DRAFTS_SELECT).click()
            return True
        except TimeoutException:
            return False
