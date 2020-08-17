import unittest
from selenium import webdriver
import time

link1 = 'http://suninjuly.github.io/registration1.html'
link2 = 'http://suninjuly.github.io/registration2.html'


class TestRegistration(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def test_registration1(self):
        browser = self.browser
        browser.get(link1)

        # Заполняет обязательные поля
        input1 = browser.find_element_by_class_name('form-control.first:required')
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_class_name('form-control.second:required')
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_class_name('form-control.third:required')
        input3.send_keys("PI@email.ru")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

    def test_registration2(self):
        browser = self.browser
        browser.get(link2)

        # Заполняет обязательные поля
        input1 = browser.find_element_by_class_name('form-control.first:required')
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_class_name('form-control.second:required')
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_class_name('form-control.third:required')
        input3.send_keys("PI@email.ru")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

    def tearDown(self):
        self.browser.close()


if __name__ == "__main__":
    unittest.main()
