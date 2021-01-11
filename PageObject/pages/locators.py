from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    EMAIL_FIELD = (By.ID, 'id_login-username')
    PASSWORD_FIELD = (By.ID, 'id_login-password')


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')
    BOOK_NAME = (By.XPATH, '// *[ @ id = "content_inner"] / article / div[1] / div[2] / h1')
    BOOK_PRICE = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/p[1]')
    SUCCESS_TEXT = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    PRICE_BASKET = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')
    SUCCESS_MESSAGE = (By.XPATH, '//*[@id="messages"]/div[1]/div')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_PAGE_LINK = (By.XPATH, '//*[@id="default"]/header/div[1]/div/div[2]/span/a')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    BASKET_IS_EMPTY_TEXT = (By.XPATH, '//*[@id="content_inner"]/p')

