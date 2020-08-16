import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select


try:
    url = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(url)

    # находим числа и считаем их сумму
    num_1 = int(browser.find_element_by_id("num1").text)
    num_2 = int(browser.find_element_by_id("num2").text)
    sum_num = str(num_1 + num_2)

    # открыть выпадающий список и найти число с ответом
    select_num_element = Select(browser.find_element_by_tag_name("select"))
    select_value_element = select_num_element.select_by_visible_text(sum_num)

    # ищем кнопку submit и кликаем в нее
    button_submit_element = browser.find_element_by_class_name("btn.btn-default")
    button_submit_element.click()

finally:
    time.sleep(10)
    browser.quit()

