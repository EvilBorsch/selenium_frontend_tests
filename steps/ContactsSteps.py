from steps.BaseSteps import BaseSteps


class ContactsSteps(BaseSteps):
    add_phone_popup_title = '//*[@data-test-id="recovery-preview-addPhone-header"]'
    add_email_popup_title = '//*[@data-test-id="recovery-preview-addEmail-header"]'

    phone_add_button = '//button[@data-test-id="recovery-addPhone-button"]'
    email_add_button = '//button[@data-test-id="recovery-addEmail-button"]'
    delete_email_button = '//button[@data-test-id="recovery-delete-email-button"]'

    phone_input = '//input[@data-test-id="phone-input"]'
    email_input = '//input[@data-test-id="recovery-addEmail-emailField-input"]'
    phone_input_error = '//*[@data-test-id="recovery-error-invalidPhone"]/span'
    
    close_popup_button = '//*[@data-test-id="cross"]'
    cancle_popup_button = '//button[@data-test-id="recovery-addPhone-cancel"]'
    phone_submit_button = '//button[@data-test-id="recovery-addPhone-submit"]'
    email_submit_button = '//button[@data-test-id="recovery-addEmail-submit"]'

    backup_email_element = '//*[@data-test-id="recovery-emails-list-block"]/div'

    def click_add_email_button(self):
        self.wait_until_and_get_elem_by_xpath(self.email_add_button).click()

    def click_add_phone_button(self):
        self.wait_until_and_get_elem_by_xpath(self.phone_add_button).click()
    
    def click_delete_email_button(self):
        self.wait_until_and_get_elem_by_xpath(self.delete_email_button).click()
    
    def click_close_popup_button(self):
        self.wait_until_and_get_elem_by_xpath(self.close_popup_button).click()

    def click_cancle_popup_button(self):
        self.wait_until_and_get_elem_by_xpath(self.cancle_popup_button).click()

    def submit_phone_form_button(self):
        self.wait_until_and_get_elem_by_xpath(self.phone_submit_button).click()

    def submit_email_form_button(self):
        self.wait_until_and_get_elem_by_xpath(self.email_submit_button).click()

    def set_phone_input(self, phone):
        self.wait_until_and_get_elem_by_xpath(self.phone_input).send_keys(phone)

    def set_email_input(self, email):
        self.wait_until_and_get_elem_by_xpath(self.email_input).send_keys(email)

    def get_phone_input_error(self):
        return self.wait_until_and_get_elem_by_xpath(self.phone_input_error).text

    def has_backup_email(self):
        return self.wait_until_and_get_elem_by_xpath(self.backup_email_element)

    def has_not_backup_email(self):
        return self.wait_until_and_check_invisibility_of_element(self.backup_email_element)

    def is_add_email_popup_title_invisible(self):
        return self.wait_until_and_check_invisibility_of_element(self.add_email_popup_title)

    def is_add_phone_popup_title_invisible(self):
        return self.wait_until_and_check_invisibility_of_element(self.add_phone_popup_title)

    def is_add_email_popup_title_visible(self):
        return not self.wait_until_and_get_elem_by_xpath(self.add_email_popup_title) is None

    def is_add_phone_popup_title_visible(self):
        return not self.wait_until_and_get_elem_by_xpath(self.add_phone_popup_title) is None

    def is_add_phone_popup_title_close(self):
        return not self.wait_until_and_check_invisibility_of_element(self.add_phone_popup_title) is None

