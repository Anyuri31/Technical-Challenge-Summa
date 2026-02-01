from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):

    CART_LINK = (By.ID, "cartur")
    CART_ITEMS = (By.CSS_SELECTOR, "tr.success")

    PLACE_ORDER_BUTTON = (By.XPATH, "//button[text()='Place Order']")
    ORDER_MODAL = (By.ID, "orderModal")

    NAME_INPUT = (By.ID, "name")
    COUNTRY_INPUT = (By.ID, "country")
    CITY_INPUT = (By.ID, "city")
    CARD_INPUT = (By.ID, "card")
    MONTH_INPUT = (By.ID, "month")
    YEAR_INPUT = (By.ID, "year")

    PURCHASE_BUTTON = (By.XPATH, "//button[text()='Purchase']")
    SUCCESS_MESSAGE = (By.XPATH, "//h2[text()='Thank you for your purchase!']")

    def open_cart(self):
        self.click_element(self.CART_LINK)

    def has_products(self):
        items = self.wait_for_find_elements(*self.CART_ITEMS)
        return len(items) > 0

    def open_place_order_modal(self):
        self.click_element(self.PLACE_ORDER_BUTTON)
        return self.wait_for_element(self.ORDER_MODAL).is_displayed()

    def fill_purchase_form(self):
        self.type_text(self.NAME_INPUT, "Anyuri Nathalia")
        self.type_text(self.COUNTRY_INPUT, "Colombia")
        self.type_text(self.CITY_INPUT, "Bogotá")
        self.type_text(self.CARD_INPUT, "4111111111111111")
        self.type_text(self.MONTH_INPUT, "12")
        self.type_text(self.YEAR_INPUT, "2026")

    def confirm_purchase(self):
        self.click_element(self.PURCHASE_BUTTON)
        return self.wait_for_element(self.SUCCESS_MESSAGE).is_displayed()
