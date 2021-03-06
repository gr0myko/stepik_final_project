from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group .btn-default:first-child")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD1_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD2_INPUT = (By.CSS_SELECTOR, "#id_registration-password2")
    LOGIN_BTN = (By.CSS_SELECTOR, '[name="registration_submit"]')

class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ALERT_NAME = (By.CSS_SELECTOR, "div.alert:first-child strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    ALERT_PRICE = (By.CSS_SELECTOR, ".alertinner p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert:first-child")

class BasketPageLocators():
    BASKET_SUMMARY = (By.CSS_SELECTOR, ".basket_summary")
    BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
    

