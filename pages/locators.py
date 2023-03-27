from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    email_input = (By.CSS_SELECTOR, '[id="id_registration-email"]')
    password1_input = (By.CSS_SELECTOR, '[id="id_registration-password1"]')
    password2_input = (By.CSS_SELECTOR, '[id="id_registration-password2"]')
    register_button = (By.CSS_SELECTOR, '[name="registration_submit"]')
    login_page_link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, '[class="btn btn-lg btn-primary btn-add-to-basket"]')
    PRODUCT_NAME = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/h1')
    PRODUCT_NAME_IN_BASKET = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '[class="price_color"]')
    PRODUCT_PRICE_IN_BASKET = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1)")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, '//*[@id="default"]/header/div[1]/div/div[2]/span/a')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, '[id="content_inner"]')
    PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, '[class="col-sm-6 h3"]')
