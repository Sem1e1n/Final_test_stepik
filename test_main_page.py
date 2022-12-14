from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
"""
def test_guest_can_go_to_login_page(browser):
    #
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    login_page = page.go_to_login_page()
    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    #
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
    
def test_guest_can_add_product_to_cart(browser):
    # метод для добавленя товара в корзину, проверки названия и цены товара
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    product_page.add_item_to_bascket()
    product_page.solve_quiz_and_get_code()
    product_page.check_add_item_to_basket()
  
   
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    #Гость открывает главную страницу 
    #Переходит в корзину по кнопке в шапке сайта
    #Ожидаем, что в корзине нет товаров
    #Ожидаем, что есть текст о том что корзина пуста 
    page = MainPage(browser, link)
    page.open()
    page.should_be_btn_basket()
    page.go_to_basket_page()

    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
    """
    
