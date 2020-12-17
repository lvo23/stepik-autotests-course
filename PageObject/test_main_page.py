"""Основная идея состоит в том, что каждую страницу веб-приложения можно описать в виде объекта класса. Способы
взаимодействия пользователя со страницей можно описать с помощью методов класса. В идеале тест, который будет
использовать Page Object, должен описывать бизнес-логику тестового сценария и скрывать Selenium-методы взаимодействия
с браузером и страницей. При изменениях в верстке страницы не придется исправлять тесты, связанные с этой страницей.
Вместо этого нужно будет поправить только класс, описывающий страницу. """

"""Важно! Обычно методы у Page Object бывают двух типов: сделать что-то и проверить что-то.
"""

from .pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.open()  # открываем страницу
    page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина

    browser.get(link)
    go_to_login_page(browser)


def go_to_login_page(browser):
    login_link = browser.find_element_by_css_selector('#login_link')
    login_link.click()
