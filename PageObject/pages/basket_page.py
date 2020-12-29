from .base_page import BasePage
from .locators import BasePageLocators
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def go_to_basket_page(self):
        basket_page_link = self.browser.find_element(*BasePageLocators.BASKET_PAGE_LINK)
        basket_page_link.click()

    def should_be_basket_url(self):
        assert '/basket' in self.browser.current_url, 'basket not in current url'

    def should_be_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_TEXT), 'Basket is not empty'

    def should_be_basket_is_empty_text(self):
        assert 'Ваша корзина пуста' in self.browser.find_element(*BasketPageLocators.BASKET_IS_EMPTY_TEXT).text, \
            "Missing text 'Ваша корзина пуста'"
