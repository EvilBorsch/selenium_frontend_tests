from pages.BasePage import Page
from steps.authSteps import *
from steps.PasswordPopupSteps import PasswordPopupSteps
from pages.SecurityPage import SecurityPage
import time

class PasswordPopup(Page):
    PATH = 'security'

    def is_password_changed(self):
        password_steps = PasswordPopupSteps(self.driver)

        return not password_steps.get_popup_password_chnged() is None


    def open(self, url=None):
        super().open(url)
        security_page = SecurityPage(self.driver)
        security_page.click_setPassword_link()

    def change_new_password_visibility(self):
        password_steps = PasswordPopupSteps(self.driver)
        password_steps.toggle_new_password_visibility()

    def change_old_password_visibility(self):
        password_steps = PasswordPopupSteps(self.driver)
        password_steps.toggle_old_password_visibility()


    def set_new_password_and_get_password_security_value(self, password):
        password_steps = PasswordPopupSteps(self.driver)
        
        password_steps.clean_new_password()
        password_steps.set_new_password_value(password)

        time.sleep(0.5)
        text = self.get_new_password_security()

        password_steps.clean_new_password()

        return text

    def get_new_password_security(self):
        password_steps = PasswordPopupSteps(self.driver)
        password_steps.focus_new_password_input()
        return password_steps.get_new_password_security()


    def change_password(self, old, new):
        self.change_fields(old, new)

        self.submit_form()

    def change_fields(self, old, new):
        password_steps = PasswordPopupSteps(self.driver)

        password_steps.set_old_password_value(old)
        password_steps.set_new_password_value(new)
        password_steps.set_repeat_password_value(new)

    def is_old_password_visibile(self):
        password_steps = PasswordPopupSteps(self.driver)

        return password_steps.get_current_password_input_type() == 'text'

    def is_new_password_visible(self):
        password_steps = PasswordPopupSteps(self.driver)

        return (password_steps.get_new_password_input_type() == 'text') and (password_steps.get_repeat_password_input_type() == 'text')

       
    def submit_form(self):
        password_steps = PasswordPopupSteps(self.driver)

        password_steps.submit_change_password()


    def send_empty_form(self):
        password_steps = PasswordPopupSteps(self.driver)

        password_steps.submit_change_password()


    def send_form_with_uncorrect_repeat(self, new, old):
        password_steps = PasswordPopupSteps(self.driver)

        password_steps.set_old_password_value(old)
        password_steps.set_new_password_value(new)
        password_steps.set_repeat_password_value(new + old)

        password_steps.submit_change_password()

    def close_popup(self):
        password_steps = PasswordPopupSteps(self.driver)

        password_steps.close_change_password()

    def cancel(self):
        password_steps = PasswordPopupSteps(self.driver)

        password_steps.cancel_change_password()

    def is_new_password_error(self):
        password_steps = PasswordPopupSteps(self.driver)
        return password_steps.is_new_password_invalid()

    def is_current_password_error(self):
        password_steps = PasswordPopupSteps(self.driver)
        return password_steps.is_current_password_invalid()

    def is_repeat_password_error(self):
        password_steps = PasswordPopupSteps(self.driver)
        return password_steps.is_repeat_password_invalid()

    def generate_password(self):
        password_steps = PasswordPopupSteps(self.driver)

        password_steps.click_generate_link()

    def get_new_password_value(self):
        password_steps = PasswordPopupSteps(self.driver)
        return password_steps.get_new_password_value()

    def get_repeat_password_value(self):
        password_steps = PasswordPopupSteps(self.driver)
        return password_steps.get_repeat_password_value()

    def is_popup_open(self):
        password_steps = PasswordPopupSteps(self.driver)
        return not password_steps.is_popup_unvisible()



        





