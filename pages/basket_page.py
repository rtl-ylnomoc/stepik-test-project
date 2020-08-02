from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM_FORM), 'Products should not be in the basket'

    def should_be_basket_empty_text(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), 'No empty basket text'
