from .BaseSteps import *


class PersonaInfoSteps(BaseSteps):
    personal_info_button_path = '//*[@id="root"]/div/div[3]/div/div[2]/div[1]/div/div[2]/a/div/a'
    personal_data_header = '//*[@id="root"]/div/div[3]/div/div/h1'
    contacts_header = '//*[@id="root"]/div/div[3]/div/div/h1'
    all_settings_button_path = '//*[@id="root"]/div/div[3]/div/div[2]/div[2]/div/div[2]/a/div/a'
    name_surname_left_card_path = '//*[@id="root"]/div/div[3]/div/div[2]/div[1]/div/div[1]/div[3]/div[1]/div[1]/div[2]/div/p'
    name_surname_left_bar_path = '//*[@id="root"]/div/div[2]/div/div[1]/div/div[4]/h3'
    add_reserve_email = '//*[@id="root"]/div/div[3]/div/div[2]/div[2]/div/div[1]/div[3]/div/div[4]/div[2]/a'
    reserve_email_header_pop_up = '/html/body/div[2]/div[2]/div/div/div[2]/form/div[1]/h1/span'
    confirm_reserve_email_btn_path = '/html/body/div[2]/div[2]/div/div/div[2]/form/button[1]/span'
    input_reserver_email = '/html/body/div[2]/div[2]/div/div/div[2]/form/div[4]/div/div/div/input'
    result_email_span = '/html/body/div[2]/div[2]/div/div/div[2]/form/div[4]/div[2]/small/span'
    correct_email_header = '/html/body/div[2]/div[2]/div/div/div[2]/div/h1'
    delete_email_path = '//*[@id="root"]/div/div[3]/div/div/div[10]/div/div[2]/div/div[3]/button'
    confirm_delete_email_button = '/html/body/div[2]/div[2]/div/div/div[2]/form/button[1]'

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

    def click_add_reserve_email(self):
        """
                :return: Текст хедера в pop up добавления почты
        """
        self.wait_until_and_get_elem_by_xpath(self.add_reserve_email).click()
        return self.wait_until_and_get_elem_by_xpath(self.reserve_email_header_pop_up).text

    def click_confirm_email(self):
        self.wait_until_and_get_elem_by_xpath(self.confirm_reserve_email_btn_path).click()

    def insert_reserve_email(self, email):
        self.wait_until_and_get_elem_by_xpath(self.input_reserver_email).send_keys(email)

    def check_input_email_result(self) -> str:
        """
        :return: Что произошло после ввода email
        """
        return self.wait_until_and_get_elem_by_xpath(self.result_email_span).text

    def get_correct_email_header(self) -> str:
        return self.wait_until_and_get_elem_by_xpath(self.correct_email_header).text

    def click_delete_reserve_email_btn(self):
        self.wait_until_and_get_elem_by_xpath(self.delete_email_path).click()

    def click_confirm_button(self):
        self.wait_until_and_get_elem_by_xpath(self.confirm_delete_email_button).click()

    def clear_email(self):
        self.wait_until_and_get_elem_by_xpath(self.input_reserver_email).clear()
