from steps.BaseSteps import BaseSteps


class SecuritySteps(BaseSteps):
    devices_page_title = '//*[@data-test-id="caption-text"]'
    devices_link = '//*[@data-test-id="device-and-apps-item"]'
    
    services_link = '//*[@data-test-id="external-services-item"]'
    services_page_title = '//*[@data-test-id="oauth-applications"]/div/h1'
    
    history_link = '//*[@data-test-id="actions-history-item"]'
    history_page_title = '//*[@data-test-id="settings-actions"]/div[1]/h1'
    
    setpassword_button = '//*[@data-test-id="password-action"]'
    setpassword_page_title = '//*[@data-test-id="popup-wrapper"]'
    
    keys_page_title = '//*[@data-test-id="caption"]'
    keys_link = '//*[@data-test-id="electronic-keys-item"]'

    oauth2_link = '//*[@data-test-id="twofa-item"]'
    oauth2_page_title = '//*[@class="b-panel__header__text"]'

    password_more_link = '//*[@data-test-id="password-item"]//*[@data-test-id="item-details"]'
    password_more_page_title = '//div[@class="h-header__text"]'

    keys_more_link = '//*[@data-test-id="electronic-keys-item"]//*[@data-test-id="item-details"]'
    keys_more_page_title = '//div[@class="h-header__text"]'

    twofact_more_link = '//*[@data-test-id="twofa-item"]//*[@data-test-id="item-details"]'
    twofact_more_page_title = '//div[@class="h-header__text"]'


    def click_devices_link(self):
        self.wait_until_and_get_elem_by_xpath(self.devices_link).click()
        return self.wait_until_and_get_elem_by_xpath(self.devices_page_title).text

    def click_services_link(self):
        self.wait_until_and_get_elem_by_xpath(self.services_link).click()
        return self.wait_until_and_get_elem_by_xpath(self.services_page_title).text

    def click_history_link(self):
        self.wait_until_and_get_elem_by_xpath(self.history_link).click()
        window_before = self.driver.window_handles[0]
        window_after = self.driver.window_handles[1]
        self.driver.switch_to_window(window_after)
        text = self.wait_until_and_get_elem_by_xpath(self.history_page_title).text
        self.driver.close()
        self.driver.switch_to_window(window_before)
        return text

    def click_password_more_link(self):
        self.wait_until_and_get_elem_by_xpath(self.password_more_link).click()
        window_before = self.driver.window_handles[0]
        window_after = self.driver.window_handles[1]
        self.driver.switch_to_window(window_after)
        text = self.wait_until_and_get_elem_by_xpath(self.password_more_page_title).text
        self.driver.close()
        self.driver.switch_to_window(window_before)
        return text

    def click_twofact_more_link(self):
        self.wait_until_and_get_elem_by_xpath(self.twofact_more_link).click()
        return self.wait_until_and_get_elem_by_xpath(self.twofact_more_page_title).text
        

    def click_keys_more_link(self):
        self.wait_until_and_get_elem_by_xpath(self.keys_more_link).click()
        return self.wait_until_and_get_elem_by_xpath(self.keys_more_page_title).text

    def click_setpassword_link(self):
        self.wait_until_and_get_elem_by_xpath(self.setpassword_button).click()
        return self.wait_until_and_get_elem_by_xpath(self.setpassword_page_title)

    def click_keys_link(self):
        self.wait_until_and_get_elem_by_xpath(self.keys_link).click()
        return self.wait_until_and_get_elem_by_xpath(self.keys_page_title).text

    def click_oauth_link(self):
        self.wait_until_and_get_elem_by_xpath(self.oauth2_link).click()
        return self.wait_until_and_get_elem_by_xpath(self.oauth2_page_title).text

     