from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    URL = "https://www.demoblaze.com/"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)

    def select_category(self, category_name):
        category = self.wait.until(
            EC.element_to_be_clickable(
                (By.LINK_TEXT, category_name)
            )
        )
        category.click()

    def select_product(self, product_name):
        product = self.wait.until(
            EC.element_to_be_clickable(
                (By.LINK_TEXT, product_name)
            )
        )
        product.click()
