# pytest -s test_product_page.py
import time

import pytest

from .pages.product_page import ProductPage


@pytest.mark.parametrize('link', [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                 marks=pytest.mark.xfail),
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9",
])
# @pytest.mark.parametrize('promo_offer', ["0", "1", "3", "4", "5", "6", "7", "8", "9"])
def test_guest_can_add_product_to_basket(browser, link):
    # link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"  # Товар №1
    # link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'  # Товар №2
    page = ProductPage(browser,
                       link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.add_to_basket()  # выполняем метод страницы — добавляем товар в корзину
    page.solve_quiz_and_get_code()
    page.checking_notification_of_adding()  # Проверка наличия уведомления
    page.checking_product_name()  # Проверка названия товара
    page.checking_price()  # Проверка совпадения цены
    # time.sleep(10)  # Просто посмотреть
