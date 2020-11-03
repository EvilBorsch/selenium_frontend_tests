import time

import pyautogui

from .BaseSteps import *


class InputAnnotationsErrors:
    def __init__(self, name_err: str, last_name_err: str, nickname_err: str, city_err: str):
        self.name_err = name_err
        self.last_name_err = last_name_err
        self.nickname_err = nickname_err
        self.city_err = city_err


class PersonalDataSteps(BaseSteps):
    change_btn_path = '//*[@id="root"]/div/div[3]/div/div/div/form/div/div[1]/div/div/div[2]/button'
    avatar_path = '//*[@id="root"]/div/div[3]/div/div/div/form/div/div[1]/div/div/div[1]/div[2]'
    name_path = '/html/body/div/div[1]/div[3]/div/div[3]/div/div/div/form/div/div[2]/div[1]/div/div[2]/div/div/input'
    last_name_path = '/html/body/div/div[1]/div[3]/div/div[3]/div/div/div/form/div/div[2]/div[2]/div/div[2]/div/div/input'
    nickname_path = '/html/body/div/div[1]/div[3]/div/div[3]/div/div/div/form/div/div[2]/div[3]/div/div[2]/div/div/input'
    city_path = '/html/body/div/div[1]/div[3]/div/div[3]/div/div/div/form/div/div[2]/div[6]/div[2]/div/div/input'
    submit_btn_path = '/html/body/div/div[1]/div[3]/div/div[3]/div/div/div/form/div/div[2]/button[1]'
    name_err_path = '//*[@id="root"]/div/div[3]/div/div/div/form/div/div[2]/div[1]/div/div[3]/small'
    last_name_err_path = '//*[@id="root"]/div/div[3]/div/div/div/form/div/div[2]/div[2]/div/div[3]/small'
    nickname_err_path = '//*[@id="root"]/div/div[3]/div/div/div/form/div/div[2]/div[3]/div/div[3]/small'
    city_err_path = '//*[@id="root"]/div/div[3]/div/div/div/form/div/div[2]/div[6]/div[3]/small'
    submit_change_avatar_paht = '/html/body/div[2]/div[2]/div/div[2]/div/button[1]'
    upload_process = '//*[@id="root"]/div/div[3]/div/div/div/form/div/div[1]/div/div/div[1]/div[2]/div[1]'
    photo_ready = '//*[@id="root"]/div/div[3]/div/div/div/form/div/div[1]/div/div/div[1]/div[2]'

    def upload_avatar(self, path: str):
        time.sleep(2)
        splited = path.split('/')
        last_el = len(splited) - 1
        file_name = splited[last_el]
        directory_path = '/'.join(splited[0:last_el])

        pyautogui.write('/')
        time.sleep(2)

        pyautogui.write(directory_path[1:] + '/', interval=0.15)
        pyautogui.press('return')
        time.sleep(2)

        pyautogui.write(file_name, interval=0.15)
        pyautogui.press('return')

    def click_submit_avatar_btn(self):
        self.wait_until_and_get_elem_by_xpath(self.submit_change_avatar_paht).click()

    def click_on_change_button(self):
        self.wait_until_and_get_elem_by_xpath(self.change_btn_path).click()

    def click_on_avtar(self):
        self.wait_until_and_get_elem_by_xpath(self.avatar_path).click()

    def fill_name(self, name):
        self.fill_input(self.name_path, name)

    def fill_last_name(self, last_name):
        self.fill_input(self.last_name_path, last_name)

    def fill_nickanme(self, nickname):
        self.fill_input(self.nickname_path, nickname)

    def fill_city(self, city):
        self.fill_input(self.city_path, city)

    def collect_errors(self) -> InputAnnotationsErrors:
        """
        :return: Возвращает структуру с ошибками в процессе заполнения формы
        """
        name_err = self.get_element_text(self.name_err_path)
        last_name_err = self.get_element_text(self.last_name_err_path)
        nickname_err = self.get_element_text(self.nickname_err_path)
        city_err = self.get_element_text(self.city_err_path)
        return InputAnnotationsErrors(name_err, last_name_err, nickname_err, city_err)

    def click_submit(self) -> InputAnnotationsErrors:
        btn = self.wait_until_and_get_elem_by_xpath(self.submit_btn_path)
        btn.click()
        return self.collect_errors()

    def check_if_uploaded(self):
        try:
            self.wait_until_and_get_elem_by_xpath(self.upload_process)
            print("ok")
        except TimeoutError:
            return False
        try:
            self.wait_until_and_get_elem_by_xpath(self.photo_ready)
            print("ok")
            return True
        except TimeoutError:
            return False
