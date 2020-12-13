"""
pytest -s -v -m "not smoke" test_fixture8.py
чтобы запустить все тесты, не смоук - инверсия

pytest -s -v -m "smoke or regression" test_fixture8.py
для запуска смоука и регресса

pytest -s -v -m "smoke and win10" test_fixture8.py
запустит тесты, у которых обе эти маркировки

ещё есть @pytest.mark.skip и skipif  для пропуска тестов - который ожидаемо упадёт из-за наличия бага, чтобы он не влиял
на результаты прогона всех тестов. Эти метки не требуют дополнительного объявления в pytest.ini. """

import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1:

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    @pytest.mark.smoke
    @pytest.mark.win10
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")