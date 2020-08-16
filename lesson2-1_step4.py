import time
import math
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    url = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(url)

    # считывает значение переменной х со страницы
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    # ищем поле для ввода и вводим полученное значение
    input_answer = browser.find_element_by_id("answer")
    input_answer.send_keys(y)

    # ищем чекбокс и кликаем в него
    check_robot_element = browser.find_element_by_id("robotCheckbox")
    check_robot_element.click()

    # ищем радиобаттон и кликаем в него
    radio_robot_element = browser.find_element_by_id("robotsRule")
    radio_robot_element.click()

    # ищем кнопку submit и кликаем в нее
    button_submit_element = browser.find_element_by_class_name("btn.btn-default")
    button_submit_element.click()

finally:
    time.sleep(10)
    browser.quit()

