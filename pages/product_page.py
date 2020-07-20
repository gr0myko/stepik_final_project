from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        button.click()
    
    def should_be_correct_product_in_basket(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        alert_name = self.browser.find_element(*ProductPageLocators.ALERT_NAME)
        assert alert_name.text == product_name.text, "Product name is wrong in basket"

    def should_be_correct_sum_in_basket(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        alert_price = self.browser.find_element(*ProductPageLocators.ALERT_PRICE)
        assert alert_price.text == product_price.text, "Wrong price in basket"
