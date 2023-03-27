from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def __init__(self, browser, url, timeout=10):
        super().__init__(browser, url, timeout)
        self.password = None
        self.email = None

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "'Login' word is not presented"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        self.email = email
        self.password = password

        # находим элементы на странице: поля ввода почты, пароля и кнопку регистрации
        email_input = self.browser.find_element(*LoginPageLocators.email_input)
        pass_input = self.browser.find_element(*LoginPageLocators.password1_input)
        pass_confirm = self.browser.find_element(*LoginPageLocators.password2_input)
        reg_button = self.browser.find_element(*LoginPageLocators.register_button)

        # вводим почту, пароль
        email_input.send_keys(email)
        pass_input.send_keys(password)
        pass_confirm.send_keys(password)

        # нажимаем на кнопку: зарегистрировать
        reg_button.click()

    def make_email_and_pass(self):
        # генерация почты и передача пароля
        return (str(time.time()) + "@fakemail.org", "myStrongPassword№121")
