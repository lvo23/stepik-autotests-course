import time
import math
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    url = "http://suninjuly.github.io/explicit_wait2.html"
    options = ChromeOptions()
    options.add_argument("--start-maximized")
    browser = webdriver.Chrome(options=options)
    browser.get(url)

    # ждем пока цена станет менее 100
    price_element = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    # нажимаем на кнопку
    button = browser.find_element_by_id("book")
    button.click()

    # считываем значение х и считаем формулу
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    # вводим ответ в текстовое поле
    input_answer_element = browser.find_element_by_id("answer")
    input_answer_element.send_keys(y)

    # ищем кнопку submit и кликаем в нее
    button_submit_element = browser.find_element_by_id("solve")
    button_submit_element.click()

finally:
    time.sleep(6)
    browser.quit()

