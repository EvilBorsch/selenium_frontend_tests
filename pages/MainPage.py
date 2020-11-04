from steps.MainPageSteps import *
from .BasePage import *
from steps.MainPageSteps import MainPageSteps


class Main_page(Page):
    BASE_URL = 'https://e.mail.ru/settings/folders'
    PATH = ''

    @property
    def pop3_steps(self):
        return MainPageSteps(self.driver)

    def click_change_checkbox_pop3(self) -> bool:
        """
                :return: True если checked, else False
        """
        classes_list = self.pop3_steps.toggle_checkbox_POP3()
        if len(classes_list.split()) == 2:
            return True
        return False

    def click_pencil_icon(self) -> bool:
        """
                :return: True если открылось окно
        """
        return self.pop3_steps.click_pencil_button()

    #
    # def click_get_all_settings(self) -> bool:
    #     """
    #     :return: Произошел ли удачный переход
    #     """
    #     text = self.personal_info_steps.click_all_settings()
    #     if (text == "Контакты и адреса"):
    #         return True
    #     return False
    #
    # def get_name_surname_from_left_bar(self) -> (str, str):
    #     return self.personal_info_steps.get_name_surname_from_left_bar()
    #
    # def get_name_surname_from_card(self) -> (str, str):
    #     return self.personal_info_steps.get_name_surname_from_card()
    #
    # def click_add_reserve_email(self) -> bool:
    #     """
    #     :return: Произошел ли удачный переход
    #     """
    #     text = self.personal_info_steps.click_add_reserve_email()
    #     if (text == "Добавление резервной почты"):
    #         return True
    #     return False
    #
    # def add_email(self, email) -> str:
    #     """
    #     :return: Значение хедера
    #     """
    #     self.personal_info_steps.clear_email()
    #     self.personal_info_steps.insert_reserve_email(email)
    #     self.personal_info_steps.click_confirm_email()
    #     try:
    #         return self.personal_info_steps.check_input_email_result()
    #     except Exception:
    #         return self.personal_info_steps.get_correct_email_header()
    #
    # def check_correct_email_header(self):
    #     return self.personal_info_steps.get_correct_email_header()
    #
    # def clear_reserve_email(self):
    #     self.open("https://id.mail.ru/contacts")
    #     self.personal_info_steps.click_delete_reserve_email_btn()
    #     self.personal_info_steps.click_confirm_button()
