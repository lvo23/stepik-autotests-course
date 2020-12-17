"""открыть страницу 
ввести правильный ответ 
нажать кнопку "Отправить" 
дождаться фидбека о том, что ответ правильный 
проверить, что текст в опциональном фидбеке полностью совпадает с "Correct!""""

import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestParams:
    message = ''
    urls = ['https://stepik.org/lesson/236895/step/1',
'https://stepik.org/lesson/236896/step/1',
'https://stepik.org/lesson/236897/step/1',
'https://stepik.org/lesson/236898/step/1',
'https://stepik.org/lesson/236899/step/1',
'https://stepik.org/lesson/236903/step/1',
'https://stepik.org/lesson/236904/step/1',
'https://stepik.org/lesson/236905/step/1]',

    @pytest.mark.parametrize('links', &&&&)
    def test_guest_should_see_login_link(self, browser, urls):
        link = f"{urls}"
        browser.get(link)


# ищем и нажимаем кнопку Отправить
button = browser.find_element_by_css_class_name("submit-submission")
button.click()



link = "http://selenium1py.pythonanywhere.com/"




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