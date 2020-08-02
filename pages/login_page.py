from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'Not login page'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'No login form'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'No register form'

    def register_new_user(self, email, password):
        register_email_input = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        register_email_input.send_keys(email)
        register_pass1_input = self.browser.find_element(*LoginPageLocators.REGISTER_PASS1)
        register_pass1_input.send_keys(password)
        register_pass2_input = self.browser.find_element(*LoginPageLocators.REGISTER_PASS2)
        register_pass2_input.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()
