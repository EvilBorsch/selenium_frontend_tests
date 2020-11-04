from steps.BaseSteps import BaseSteps


class PasswordPopupSteps(BaseSteps):
    current_password_input = '//input[@data-test-id="old-password-input"]'
    current_password_error_element = '//*[@data-test-id="old-password"]/div[3]'

    new_password_input = '//input[@data-test-id="new-password-input"]'
    new_password_error_element = '//*[@data-test-id="new-password"]/div[3]'

    repeat_password_input = '//input[@data-test-id="repeat-password-input"]'
    repeat_password_error_element = '//*[@data-test-id="repeat-password"]/div[3]'

    change_password_button = '//button[@data-test-id="password-change-submit"]'
    cancel_password_button = '//button[@data-test-id="password-change-cancel"]'
    close_password_button = '//*[@data-test-id="cross"]'

    new_password_input_visibility_elem = '//*[@data-test-id="new-password-input__tooltip-wrapper"]//*[@data-test-id="toggle-password-mask"]'
    old_password_input_visibility_elem = '//*[@data-test-id="old-password"]//*[@data-test-id="toggle-password-mask"]'

    password_security_element = '//*[@data-test-id="password-change-tooltip"]/div[1]/div/p'
    generate_link = '//*[@data-test-id="generate-password"]'

    change_password_popup ='//*[@data-test-id="password-change-panel"]'

    password_changed = '//*[@data-test-id="statuses-password-changed-panel"]'

    def get_popup_password_chnged(self):
        return self.wait_until_and_get_elem_by_xpath(self.password_changed)

    def is_popup_unvisible(self):
        return self.wait_until_and_check_invisibility_of_element(self.change_password_popup)

    def set_old_password_value(self, password):
        self.wait_until_and_get_elem_by_xpath(self.current_password_input).send_keys(password)

    def set_new_password_value(self, password):
        self.wait_until_and_get_elem_by_xpath(self.new_password_input).send_keys(password)

    def set_repeat_password_value(self, password):
        self.wait_until_and_get_elem_by_xpath(self.repeat_password_input).send_keys(password)

    def get_old_password_value(self):
        self.wait_until_and_get_elem_by_xpath(self.current_password_input).get_attribute('value')

    def get_new_password_value(self):
        self.wait_until_and_get_elem_by_xpath(self.new_password_input).get_attribute('value')

    def get_repeat_password_value(self):
        self.wait_until_and_get_elem_by_xpath(self.repeat_password_input).get_attribute('value')

    def submit_change_password(self):
        self.wait_until_and_get_elem_by_xpath(self.change_password_button).click()

    def cancel_change_password(self):
        self.wait_until_and_get_elem_by_xpath(self.cancel_password_button).click()

    def close_change_password(self):
        self.wait_until_and_get_elem_by_xpath(self.close_password_button).click()

    def toggle_new_password_visibility(self):
        self.wait_until_and_get_elem_by_xpath(self.new_password_input_visibility_elem).click()

    def toggle_old_password_visibility(self):
        self.wait_until_and_get_elem_by_xpath(self.old_password_input_visibility_elem).click()

    def get_current_password_input_type(self):
        return self.wait_until_and_get_elem_by_xpath(self.current_password_input).get_attribute('type')

    def get_new_password_input_type(self):
        return self.wait_until_and_get_elem_by_xpath(self.new_password_input).get_attribute('type')

    def get_repeat_password_input_type(self):
        return self.wait_until_and_get_elem_by_xpath(self.repeat_password_input).get_attribute('type')

    def is_current_password_invalid(self):
        return  not (self.wait_until_and_get_elem_by_xpath(self.current_password_error_element) is None)

    def is_new_password_invalid(self):
        return  not (self.wait_until_and_get_elem_by_xpath(self.new_password_error_element) is None)

    def is_repeat_password_invalid(self):
        return not (self.wait_until_and_get_elem_by_xpath(self.repeat_password_error_element) is None)

    def focus_new_password_input(self):
        self.wait_until_and_get_elem_by_xpath(self.new_password_input).click()

    def get_new_password_security(self):
        return self.wait_until_and_get_elem_by_xpath(self.password_security_element).text

    def clean_old_password(self):
        self.wait_until_and_get_elem_by_xpath(self.current_password_input).send_keys('')

    def clean_new_password(self):
        self.wait_until_and_get_elem_by_xpath(self.new_password_input).send_keys('')

    def clean_repeat_password(self):
        self.wait_until_and_get_elem_by_xpath(self.repeat_password_input).send_keys('')

    def click_generate_link(self):
        self.wait_until_and_get_elem_by_xpath(self.generate_link).click()
