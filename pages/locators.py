from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    VIEW_BASKET = (By.CSS_SELECTOR, '.basket-mini > .btn-group > a.btn')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    pass


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTER_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTER_PASS1 = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTER_PASS2 = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_BUTTON = (By.CSS_SELECTOR, 'button[name="registration_submit"]')


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    ALERT_ITEM_NAME = (By.CSS_SELECTOR, '.alert-success > .alertinner > strong')
    ITEM_NAME = (By.CSS_SELECTOR, '#content_inner > .product_page > .row > .product_main > h1')
    BASKET_TOTAL = (By.CSS_SELECTOR, '.alert > .alertinner > p > strong')
    ITEM_COST = (By.CSS_SELECTOR, '#content_inner > .product_page > .row > .product_main > .price_color')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success:first-child')


class BasketPageLocators():
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, '#content_inner > p')
    BASKET_ITEM_FORM = (By.CSS_SELECTOR, '#basket_formset')
