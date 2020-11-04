from components.base import BaseComponent


class PasswordForm(BaseComponent):
    PASSWORD_INPUT = '//input[@data-test-id="password"]'
    RE_PASSWORD_INPUT = '//input[@data-test-id="passwordRepeat"]'
    SECRET_QUESTION_INPUT = '//input[@data-test-id="question"]'
    QUESTION_ANSWER_INPUT = '//input[@data-test-id="answer"]'
    CURRENT_PASSWORD_INPUT = '//input[@data-test-id="userPassword"]'
    SAVE_BUTTON = '//button[@data-test-id="submit"]'
    BACK_BUTTON = '//button[@data-test-id="cancel"]'
    CLOSE_CREATE_FOLDER_BUTTON = '//div[@data-test-id="cross"]'

    INVALID_PASSWORD_ERROR = '//small[@data-test-id="password-error-text"]'
    INVALID_RE_PASSWORD_ERROR = '//small[@data-test-id="passwordRepeat-error-text"]'
    INVALID_SECRET_QUESTION_ERROR = '//small[@data-test-id="question-error-text"]'
    INVALID_SECRET_QUESTION_ANSWER_ERROR = '//small[@data-test-id="answer-error-text"]'
    INVALID_USER_PASSWORD_ERROR = '//small[@data-test-id="userPassword-error-text"]'

    def set_password(self, password):
        self.wait_until_and_get_elem_by_xpath(self.PASSWORD_INPUT).send_keys(password)

    def set_re_password(self, re_password):
        self.wait_until_and_get_elem_by_xpath(self.RE_PASSWORD_INPUT).send_keys(re_password)

    def set_question(self, question):
        self.wait_until_and_get_elem_by_xpath(self.SECRET_QUESTION_INPUT).send_keys(question)

    def set_question_answer(self, answer):
        self.wait_until_and_get_elem_by_xpath(self.QUESTION_ANSWER_INPUT).send_keys(answer)

    def set_current_password(self, current_password):
        self.wait_until_and_get_elem_by_xpath(self.CURRENT_PASSWORD_INPUT).send_keys(current_password)

    def save(self):
        self.wait_until_and_get_elem_by_xpath(self.SAVE_BUTTON).click()

    def back(self):
        self.wait_until_and_get_elem_by_xpath(self.BACK_BUTTON).click()

    def close(self):
        self.wait_until_and_get_elem_by_xpath(self.CLOSE_CREATE_FOLDER_BUTTON).click()

    @property
    def invalid_password_error(self):
        return len(self.driver.find_elements_by_xpath(self.INVALID_PASSWORD_ERROR)) != 0

    @property
    def invalid_re_password_error(self):
        return len(self.driver.find_elements_by_xpath(self.INVALID_RE_PASSWORD_ERROR)) != 0

    @property
    def invalid_secret_question_error(self):
        return len(self.driver.find_elements_by_xpath(self.INVALID_SECRET_QUESTION_ERROR)) != 0

    @property
    def invalid_secret_question_answer_error(self):
        return len(self.driver.find_elements_by_xpath(self.INVALID_SECRET_QUESTION_ANSWER_ERROR)) != 0

    @property
    def invalid_user_password_error(self):
        return len(self.driver.find_elements_by_xpath(self.INVALID_USER_PASSWORD_ERROR)) != 0
