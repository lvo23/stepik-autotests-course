import time
import math
from selenium import webdriver
from selenium.webdriver import ChromeOptions


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    url = "http://suninjuly.github.io/execute_script.html"
    options = ChromeOptions()
    options.add_argument("--start-maximized")
    browser = webdriver.Chrome(options=options)
    browser.get(url)

    # считываем значение х и считаем формулу
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    # скроллим страницу вниз

    browser.execute_script("window.scrollBy(0, 150);")

    # вводим ответ в текстовое поле
    input_answer_element = browser.find_element_by_id("answer")
    input_answer_element.send_keys(y)

    # отмечаем чекбокс
    check_robot_element = browser.find_element_by_id("robotCheckbox")
    check_robot_element.click()

    # выбираем радиобаттон
    radio_robot_element = browser.find_element_by_id("robotsRule")
    radio_robot_element.click()

    # ищем кнопку submit и кликаем в нее
    button_submit_element = browser.find_element_by_class_name("btn-primary")
    button_submit_element.click()

finally:
    time.sleep(6)
    browser.quit()

