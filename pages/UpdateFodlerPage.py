from steps.UpdateFolderSteps import UpdateFolderSteps
from .BasePage import *


class UpdateFolderPage(Page):
    BASE_URL = 'https://e.mail.ru/settings/folders'
    PATH = ''

    @property
    def update_steps(self):
        return UpdateFolderSteps(self.driver)

    def close_with_cross(self) -> bool:
        header_text = self.update_steps.click_cross_button()
        return header_text == "" or False

    def close_with_cancel(self) -> bool:
        header_text = self.update_steps.click_cancel_button()
        return header_text == "" or False

    def save_changes(self) -> bool:
        header_text = self.update_steps.click_save_button()
        return header_text == "" or False

    def fill_name(self, value: str) -> bool:
        text_in_name_input = self.update_steps.set_input_name(value)
        return text_in_name_input == value or False

    def fill_nested_folder(self, value: str) -> bool:
        value_from_drop_list = self.update_steps.set_value_of_drop_list(value)
        return value_from_drop_list == value or False

    def fill_checkbox(self, checkbox_list: dict) -> bool:
        func_map: dict = {
            "pop3": self.update_steps.toggle_checkbox_pop3,
            "archive": self.update_steps.toggle_checkbox_make_archive,
            "password": self.update_steps.toggle_checkbox_password,
        }

        for i, val in checkbox_list.items():
            # пока результат работы toggle не будет равен тому что вернет переключатель
            temp: bool = False
            if val != func_map[i]():
                temp = func_map[i]()
            if val != temp:
                return False

        return True

    def reload(self):
        self.open(self.BASE_URL)
