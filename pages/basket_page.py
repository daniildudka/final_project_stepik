from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_IN_BASKET), "Basket is not empty"

    def empty_text_was_shown(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), "Basket is not empty"
