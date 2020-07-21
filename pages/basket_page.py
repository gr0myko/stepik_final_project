from .locators import BasketPageLocators
from .base_page import BasePage

class BasketPage(BasePage):
    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_SUMMARY), \
            "Basket has products, empty basket expected"
    def should_be_empty_basket_message(self):
        basket_message = self.browser.find_element(*BasketPageLocators.BASKET_MESSAGE)
        assert "Your basket is empty." in basket_message.text, \
            "No empty basket message"