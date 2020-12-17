import time
import math
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    url = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(url)

    # находим картинку с сундуком, тянем значение атрибута и считаем формулу
    img_treasure_element = browser.find_element_by_id("treasure")
    x = img_treasure_element.get_attribute("valuex")
    y = calc(x)

    # вводим ответ в текстовое поле
    answer_field_element = browser.find_element_by_id("answer")
    answer_field_element.send_keys(y)

    # отмечаем чекбокс
    check_robot_element = browser.find_element_by_id("robotCheckbox")
    check_robot_element.click()

    # выбираем радиобаттон
    radio_robot_element = browser.find_element_by_id("robotsRule")
    radio_robot_element.click()

    # ищем кнопку submit и кликаем в нее
    button_submit_element = browser.find_element_by_class_name("btn.btn-default")
    button_submit_element.click()

finally:
    time.sleep(10)
    browser.quit()

