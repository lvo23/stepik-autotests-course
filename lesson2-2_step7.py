import os
import time
from selenium import webdriver
from selenium.webdriver import ChromeOptions

current_dir = os.path.abspath(os.path.dirname(__file__)) # получаем путь к директории текущего файла lesson...
file_path = os.path.join(current_dir, 'text.txt') # добавляем к этому пути имя файла

try:
    url = "http://suninjuly.github.io/file_input.html"
    options = ChromeOptions()
    options.add_argument("--start-maximized")
    browser = webdriver.Chrome(options=options)
    browser.get(url)

    # находим и заполняет текстовые поля
    input_first_name_element = browser.find_element_by_name("firstname")
    input_first_name_element.send_keys("Vlad")

    input_last_name_element = browser.find_element_by_name("lastname")
    input_last_name_element.send_keys("Litvinov")

    input_email_element = browser.find_element_by_name("email")
    input_email_element.send_keys("vlad@vlad.ru")

    # ищем элемент для загрузки файла и загружаем файл
    choose_file_element = browser.find_element_by_id("file")
    choose_file_element.send_keys(file_path)

    # ищем кнопку submit и кликаем в нее
    button_submit_element = browser.find_element_by_class_name("btn-primary")
    button_submit_element.click()

finally:
    time.sleep(6)
    browser.quit()

