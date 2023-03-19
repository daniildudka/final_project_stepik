from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_button.click()

    def checking_notification_of_adding(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME_IN_BASKET), "Уведомление отсувствует"

    def checking_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_name_text = product_name.text
        product_name_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET)
        product_name_in_basket_text = product_name_in_basket.text
        assert product_name_text == product_name_in_basket_text, "Название товара в корзине не совпадает"

    def checking_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        product_price_text = product_price.text
        product_price_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET)
        product_price_in_basket_text = product_price_in_basket.text
        assert product_price_text == product_price_in_basket_text, "Цена не совпадает"

