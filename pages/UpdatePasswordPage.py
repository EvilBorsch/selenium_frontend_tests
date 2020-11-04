from steps.UpdatePasswordSteps import UpdatePasswordSteps
from .BasePage import *


class UpdatePasswordPage(Page):
    BASE_URL = 'https://id.mail.ru/profile'
    PATH = ''

    @property
    def update_password_steps(self):
        return UpdatePasswordSteps(self.driver)

    def set_password(self, password_context):
        self.update_password_steps.set_password(password_context['password'])
        self.update_password_steps.set_re_password(password_context['re_password'])
        self.update_password_steps.set_question(password_context['question'])
        self.update_password_steps.set_question_answer(password_context['question_answer'])
        self.update_password_steps.set_current_password(password_context['current_password'])
        self.update_password_steps.save()

    @property
    def get_password_form_errors(self) -> dict:
        return {'invalidPassword': self.update_password_steps.invalid_password_error,
                'invalidRePassword': self.update_password_steps.invalid_re_password_error,
                'invalidSecretQuestion': self.update_password_steps.invalid_secret_question_error,
                'invalidSecretQuestionAnswer': self.update_password_steps.invalid_secret_question_answer_error,
                'invalidUserPassword': self.update_password_steps.invalid_user_password_error}
