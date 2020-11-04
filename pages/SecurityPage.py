from pages.BasePage import Page
from steps.SecuritySteps import SecuritySteps


class SecurityPage(Page):
    PATH = 'security'

    def click_devices_link(self):
        security_steps = SecuritySteps(self.driver)
        text = security_steps.click_devices_link()

        if text == "Устройства и приложения":
            return True
        return False

    def click_services_link(self):
        security_steps = SecuritySteps(self.driver)
        text = security_steps.click_services_link()

        if text == "Управление приложениями":
            return True
        return False

    def click_history_link(self):
        security_steps = SecuritySteps(self.driver)
        text = security_steps.click_history_link()

        if text == "Лог действий":
            return True
        return False

    def click_password_more_link(self):
        security_steps = SecuritySteps(self.driver)
        text = security_steps.click_password_more_link()

        if text == "Надёжный пароль":
            return True
        print(text)
        return False

    def click_keys_more_link(self):
        security_steps = SecuritySteps(self.driver)
        text = security_steps.click_keys_more_link()

        if text == "Вход по электронному ключу":
            return True
        print(text)
        return False

    def click_twofact_more_link(self):
        security_steps = SecuritySteps(self.driver)
        text = security_steps.click_twofact_more_link()

        if text == "Двухфакторная аутентификация":
            return True
        print(text)
        return False

    def click_setPassword_link(self):
        security_steps = SecuritySteps(self.driver)
        popup = security_steps.click_setpassword_link()

        if popup:
            return True
        return False

    def click_keys_link(self):
        security_steps = SecuritySteps(self.driver)
        text = security_steps.click_keys_link()

        if text == "Электронные ключи":
            return True
        return False

    def click_oauth_link(self):
        security_steps = SecuritySteps(self.driver)
        text = security_steps.click_oauth_link()

        if text == "Двухфакторная аутентификация" or text == "Добавить номер телефона":
            return True
        return False
