# pytest -s test_product_page.py
import time

import pytest
from selenium.webdriver.common.by import By
from .pages.login_page import LoginPageLocators
from .pages.basket_page import BasketPage
from .pages.main_page import MainPage
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage


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
@pytest.mark.skip
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


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link_1 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3"
    page = ProductPage(browser,
                       link_1)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.add_to_basket()  # выполняем метод страницы — добавляем товар в корзину
    page.solve_quiz_and_get_code()
    assert page.is_not_element_present(By.CSS_SELECTOR,
                                       "#messages div:nth-child(1)"), "Success message is presented, but should not be"


@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    link_1 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3"
    page = ProductPage(browser,
                       link_1)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    assert page.is_not_element_present(By.CSS_SELECTOR,
                                       "#messages div:nth-child(1)"), "Success message is presented, but should not be"


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    link_1 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3"
    page = ProductPage(browser,
                       link_1)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.add_to_basket()  # выполняем метод страницы — добавляем товар в корзину
    page.solve_quiz_and_get_code()
    assert page.is_disappeared(By.CSS_SELECTOR, "#messages div:nth-child(1)"), "Success message is not disappeared"


@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.skip
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.skip
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.go_to_basket_page()  # переходим в корзину
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()  # проверяем, что корзина пустая
    basket_page.empty_text_was_shown()  # проверяем, что текст с пустой корзиной на месте


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser, timeout=5):
        link = LoginPageLocators.login_page_link  # ссылка на страницу логина\регистрации
        self.browser = browser
        # неявное ожидание
        self.browser.implicitly_wait(timeout)
        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page = LoginPage(browser, link)
        # открываем нужную страницу
        page.open()
        # генерим тестовую почту, задаем пароль
        email, password = page.make_email_and_pass()
        # регистрируем нового пользователя
        page.register_new_user(email, password)
        # проверяем, что пользователь авторизован
        page.should_be_authorized_user()  # на деле такие проверки лучше не делать (setup не для этого)

    def test_user_cant_see_success_message(self, browser):
        link_1 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3"
        page = ProductPage(browser,
                           link_1)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        assert page.is_not_element_present(By.CSS_SELECTOR,
                                           "#messages div:nth-child(1)"), "Success message is presented, but should " \
                                                                          "not be"

    def test_user_can_add_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3'  # Товар №2
        page = ProductPage(browser,
                           link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.add_to_basket()  # выполняем метод страницы — добавляем товар в корзину
        page.solve_quiz_and_get_code()
        page.checking_notification_of_adding()  # Проверка наличия уведомления
        page.checking_product_name()  # Проверка названия товара
        page.checking_price()  # Проверка совпадения цены
        # time.sleep(10)  # Просто посмотреть
