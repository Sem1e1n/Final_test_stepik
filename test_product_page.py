from pages.product_page import ProductPage
from pages.login_page import LoginPage


import pytest
import time



def test_guest_can_add_product_to_cart(browser):
    #метод для добавленя товара в корзину, проверки названия и цены товара
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    product_page.add_item_to_bascket()
    product_page.solve_quiz_and_get_code()
    product_page.check_add_item_to_basket()


