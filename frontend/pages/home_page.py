from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from frontend.pages.base_page import BasePage


class HomePage(BasePage):
    URL = "https://www.demoblaze.com/"
    PRODUCT_CARDS = (By.CLASS_NAME, "card")
    MONITORS_CATEGORY = (By.LINK_TEXT, "Monitors")
    FIRSR_MONITOR = (By.LINK_TEXT, "Apple monitor 24")

    def open(self):
        self.driver.get(self.URL)

    def select_monitors_category(self):
        self.click_element(self.MONITORS_CATEGORY)

    def get_all_products(self):
        return self.driver.find_elements(*self.PRODUCT_CARDS)

    def get_product_price(self, product_card):
        price_text = product_card.find_element(By.TAG_NAME, "h5").text
        return int(price_text.replace("$", ""))

    def get_most_expensive_product_price(self):
        products = self.get_all_products()
        highest_price = 0

        for product in products:
            price = self.get_product_price(product)
            if price > highest_price:
                highest_price = price
        return highest_price

    def are_products_visible(self):
        products = self.wait_for_elements(self.PRODUCT_CARDS)
        return len(products) > 0

    def select_product(self, product_name):
        self.click_element((By.LINK_TEXT, product_name))
