from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    StaleElementReferenceException,
    NoSuchElementException,
)
from pages.base_page import BasePage
import time


class HomePage(BasePage):
    URL = "https://www.demoblaze.com/"
    PRODUCT_CARDS = (By.CLASS_NAME, "card")
    MONITORS_CATEGORY = (By.LINK_TEXT, "Monitors")

    def open(self):
        self.driver.get(self.URL)

    def select_monitors_category(self):
        self.click_element(self.MONITORS_CATEGORY)
        self.wait_for_find_elements(*self.PRODUCT_CARDS)

    def get_all_products(self):
        return self.driver.find_elements(*self.PRODUCT_CARDS)

    def get_product_price(self, product_card):
        try:
            price_text = product_card.find_element(By.TAG_NAME, "h5").text
            return int(price_text.replace("$", ""))
        except NoSuchElementException:
            return 0

    def get_most_expensive_product_price(self, max_retries=5):
        highest_price = 0
        product_index = None

        for attempt in range(max_retries):
            try:
                products = self.wait_for_find_elements(*self.PRODUCT_CARDS)
                if not products:
                    time.sleep(1)
                    continue
                for i, product in enumerate(products):
                    try:
                        price = self.get_product_price(product)
                        if price > highest_price:
                            highest_price = price
                            product_index = i
                    except StaleElementReferenceException:
                        continue
                if product_index is not None:
                    most_expensive_product = self.wait_for_find_elements(
                        *self.PRODUCT_CARDS
                    )[product_index]
                    try:
                        modal_close = self.driver.find_element(
                            By.CLASS_NAME, "modal-footer button"
                        )
                        modal_close.click()
                    except Exception:
                        pass
                    link = most_expensive_product.find_element(By.TAG_NAME, "a")
                    self.wait.until(lambda d: link.is_displayed() and link.is_enabled())
                    link.click()
                break
            except StaleElementReferenceException:
                # Workaround para estabilizar el DOM dinámico
                # El listado de productos se re-renderiza y causa StaleElementReference
                time.sleep(0.5)
        return highest_price

    def are_products_visible(self):
        products = self.wait_for_find_elements(*self.PRODUCT_CARDS)
        return len(products) > 0
    
    

