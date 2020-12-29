from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def click_to_add_to_basket_button(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_message_about_add(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        success_text = self.browser.find_element(*ProductPageLocators.SUCCESS_TEXT).text
        assert self.is_element_present(*ProductPageLocators.BOOK_NAME), 'Book name was not found'
        assert self.is_element_present(*ProductPageLocators.SUCCESS_TEXT), 'Success text about add book was not found'
        assert book_name == success_text, f"BOOK NAME='{book_name}' not equal SUCCESS TEXT='{success_text}'"

    def should_be_total_price(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        price_basket = self.browser.find_element(*ProductPageLocators.PRICE_BASKET).text
        assert self.is_element_present(*ProductPageLocators.BOOK_PRICE), 'Book price was not found'
        assert self.is_element_present(*ProductPageLocators.PRICE_BASKET), 'Price basket was not found'
        assert book_price == price_basket, f"BOOK PRICE='{book_price}' not equal PRICE BASKET='{price_basket}'"

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), 'Missing add to basket button'

    def should_be_promo_code(self):
        assert '?promo=newYear' in self.browser.current_url, 'Promo code newYear not in current url'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is disappear"

