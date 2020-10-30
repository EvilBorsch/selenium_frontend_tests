from steps.IdSteps import *
from .BasePage import *


class Main_page(Page):
    BASE_URL = 'https://id.mail.ru'
    PATH = ''

    @property
    def personal_info_steps(self):
        return PersonaInfoSteps(self.driver)

    def click_change_personal_info(self) -> bool:
        """
        :return: Произошел ли удачный переход на страницу смены информации
        """
        text = self.personal_info_steps.click_personal_info_settings()
        if (text == "Личные данные"):
            return True
        return False

    def click_get_all_settings(self) -> bool:
        """
        :return: Произошел ли удачный переход
        """
        text = self.personal_info_steps.click_all_settings()
        print(text)
        if (text == "Контакты и адреса"):
            return True
        return False

    def get_name_surname_from_left_bar(self) -> (str, str):
        return self.personal_info_steps.get_name_surname_from_left_bar()

    def get_name_surname_from_card(self) -> (str, str):
        return self.personal_info_steps.get_name_surname_from_card()
