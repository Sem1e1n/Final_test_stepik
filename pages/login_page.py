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
        
        
    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                 " probably unauthorised user"

    def register_new_user(self, email, password):
        """Метод регистрирует нового пользователя"""
        reg_email = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        reg_email.send_keys(email)
        reg_pass = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        reg_pass.send_keys(password)
        confirm_pass = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD)
        confirm_pass.send_keys(password)
        submit = self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT)
        submit.click()
        