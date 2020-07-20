from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ALERT_NAME = (By.CSS_SELECTOR, "div.alert:first-child strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    ALERT_PRICE = (By.CSS_SELECTOR, ".alertinner p strong")
    

