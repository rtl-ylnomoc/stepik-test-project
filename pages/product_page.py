from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_item_to_basket(self):
        add = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add.click()

    def should_be_right_alert_item_name(self):
        assert self.is_element_present(*ProductPageLocators.ALERT_ITEM_NAME), 'No product added alert'
        alert_item_name = self.browser.find_element(*ProductPageLocators.ALERT_ITEM_NAME).text
        assert self.is_element_present(*ProductPageLocators.ITEM_NAME), 'No product name'
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        assert alert_item_name == item_name, 'Wrong alert item name'

    def should_be_right_basket_total(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_TOTAL), 'No basket total alert'
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        assert self.is_element_present(*ProductPageLocators.ITEM_COST), 'No product cost'
        item_cost = self.browser.find_element(*ProductPageLocators.ITEM_COST).text
        assert basket_total == item_cost, 'Wrong basket total'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_should_disapear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message did not disappear"
