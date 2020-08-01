from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    ALERT_ITEM_NAME = (By.CSS_SELECTOR, '.alert-success > .alertinner > strong')
    ITEM_NAME = (By.CSS_SELECTOR, '#content_inner > .product_page > .row > .product_main > h1')
    BASKET_TOTAL = (By.CSS_SELECTOR, '.alert > .alertinner > p > strong')
    ITEM_COST = (By.CSS_SELECTOR, '#content_inner > .product_page > .row > .product_main > .price_color')
