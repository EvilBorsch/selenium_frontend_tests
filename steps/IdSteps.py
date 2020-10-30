from .BaseSteps import *


class PersonaInfoSteps(BaseSteps):
    personal_info_button_path = '//*[@id="root"]/div/div[3]/div/div[2]/div[1]/div/div[2]/a/div/a'
    personal_data_header = '//*[@id="root"]/div/div[3]/div/div/h1'
    contacts_header = '//*[@id="root"]/div/div[3]/div/div/h1'
    all_settings_button_path = '//*[@id="root"]/div/div[3]/div/div[2]/div[2]/div/div[2]/a/div/a'
    name_surname_left_card_path = '//*[@id="root"]/div/div[3]/div/div[2]/div[1]/div/div[1]/div[3]/div[1]/div[1]/div[2]/div/p'
    name_surname_left_bar_path='//*[@id="root"]/div/div[2]/div/div[1]/div/div[4]/h3'

    def click_personal_info_settings(self) -> str:
        """
        :return: Текст хедера в личных данных
        """
        self.wait_until_and_get_elem_by_xpath(self.personal_info_button_path).click()
        return self.wait_until_and_get_elem_by_xpath(self.personal_data_header).text

    def click_all_settings(self) -> str:
        """
        :return: Текст хедера во вкладке контакты и адреса
        """
        self.wait_until_and_get_elem_by_xpath(self.all_settings_button_path).click()
        return self.wait_until_and_get_elem_by_xpath(self.contacts_header).text

    def get_name_surname_from_card(self) -> (str, str):
        """
        :return: Получает имя и фамилию из левой карточке на главной странице
        """
        text = str(self.wait_until_and_get_elem_by_xpath(self.name_surname_left_card_path).text)
        splited = text.split(' ')
        return splited[0], splited[1]

    def get_name_surname_from_left_bar(self) -> (str, str):
        """
                :return: Получает имя и фамилию из бокового бара
        """
        text = str(self.wait_until_and_get_elem_by_xpath(self.name_surname_left_bar_path).text)
        splited = text.split(' ')
        return splited[0], splited[1]
