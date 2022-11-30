from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        #проверка: на странице должно быть: логин в url , форма логина ,форма регистрации
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        #  проверка на корректный url адрес
        assert 'login' in self.browser.current_url, 'it is not login url'
        assert True

    def should_be_login_form(self):
        #  проверка что есть форма логина
        assert self.is_element_present(By.CSS_SELECTOR, "*MainPageLocators.LOGIN_FORM"), "Login form is not presented"
        assert True

    def should_be_register_form(self):
        #  проверка что есть форма регистрации на странице
        assert self.is_element_present(By.CSS_SELECTOR, "*MainPageLocators.REGISTRY_FORM"), "regystry form is not presented"
        assert True