from .pages.basket_page import BasketPage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.locators import MainPageLocators

import pytest


"""Основная идея состоит в том, что каждую страницу веб-приложения можно описать в виде объекта класса. Способы
взаимодействия пользователя со страницей можно описать с помощью методов класса. В идеале тест, который будет
использовать Page Object, должен описывать бизнес-логику тестового сценария и скрывать Selenium-методы взаимодействия
с браузером и страницей. При изменениях в верстке страницы не придется исправлять тесты, связанные с этой страницей.
Вместо этого нужно будет поправить только класс, описывающий страницу.
 Важно! Обычно методы у Page Object бывают двух типов: сделать что-то и проверить что-то."""


@pytest.mark.login_guest
class TestLoginFormMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_guest_can_see_login_url(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()


def test_guest_can_see_login_form(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()


def test_guest_can_see_register_form(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()


def go_to_login_page(self):
    link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
    link.click()
    alert = self.browser.switch_to.alert
    alert.accept()
    #return LoginPage(browser=self.browser, url=self.browser.current_url)


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru'
    page = MainPage(browser, link)
    page.open()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.go_to_basket_page()
    basket_page.should_be_basket_url()
    basket_page.should_be_basket_is_empty()
    basket_page.should_be_basket_is_empty_text()
