from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.locators import ProductPageLocators

import pytest


# @pytest.mark.parametrize('offer_num', ['1', '2', '3', '4', '5', '6',
#                                        pytest.param('7', marks=pytest.mark.xfail), '8', '9'])
# def test_guest_can_add_product_to_basket(browser, offer_num):
#     link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer_num}"
#     page = ProductPage(browser, link)
#     page.open()
#     # page.should_be_promo_code()
#     page.click_to_add_to_basket_button()
#     page.solve_quiz_and_get_code()
#     page.should_be_message_about_add()
#     page.should_be_total_price()
#
#
# @pytest.mark.xfail(reason="because we need")
# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.click_to_add_to_basket_button()
#     page.should_not_be_success_message()
#
#
# def test_guest_cant_see_success_message(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_not_be_success_message()
#
#
# @pytest.mark.xfail(reason="because we need")
# def test_message_disappeared_after_adding_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.click_to_add_to_basket_button()
#     page.should_disappear_of_success_message()
#
#
# def test_guest_should_see_login_link_on_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_login_link()


# def test_guest_can_go_to_login_page_from_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.go_to_basket_page()
    basket_page.should_be_basket_is_empty()
    basket_page.should_be_basket_is_empty_text()


