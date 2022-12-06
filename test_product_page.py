from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from pages.main_page import MainPage


import pytest
import time


"""
def test_guest_can_add_product_to_cart(browser):
    #тест для добавленя товара в корзину, проверки названия и цены товара
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    product_page.add_item_to_bascket()
    product_page.solve_quiz_and_get_code()
    product_page.check_add_item_to_basket()



def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    #
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_bascket()
    page.should_not_be_success_message()
    
def test_guest_cant_see_success_message(browser):
    #
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


def test_message_disappeared_after_adding_product_to_basket(browser):
    #
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_bascket()
    page.should_be_success_message()
    
def test_guest_should_see_login_link_on_product_page(browser):
    #гость видит сылку на форму логина
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    #гость может перейти на страницу логина со страницы продукта
    link = 'http://selenium1py.pythonanywhere.com/catalogue/'
    page = ProductPage(browser, link)
    page.open()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
 
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    #Гость открывает главную страницу 
    #Переходит в корзину по кнопке в шапке сайта
    #Ожидаем, что в корзине нет товаров
    #Ожидаем, что есть текст о том что корзина пуста 
    link = "http://selenium1py.pythonanywhere.com/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_btn_basket()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket_message()
    """
@pytest.mark.login_guest
class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
        page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + '@fakemail.org'
        password = str(time.time())
        page.register_new_user(email=email, password=password) 
        # page.should_be_authorized_user()
        
    #                       
    def test_user_can_go_to_login_page_from_product_page(self,browser):
        #гость может перейти на страницу логина со страницы продукта
        link = 'http://selenium1py.pythonanywhere.com/catalogue/'
        page = ProductPage(browser, link)
        page.open()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_user_should_see_login_link(self,browser):
        #
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()