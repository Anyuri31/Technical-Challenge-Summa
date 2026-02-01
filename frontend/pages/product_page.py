from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductPage(BasePage):

    ADD_TO_CART_BUTTON = (By.LINK_TEXT, "Add to cart")

    def add_to_cart(self):
        self.click_element(self.ADD_TO_CART_BUTTON)
        self.accept_alert()
