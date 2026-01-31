from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def wait_for_element(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))
    
    def click_element(self, locator):
        element=self.wait_for_element(locator)
        element.click()
    
    def get_text(self, locator):
        element=self.wait_for_element(locator)
        return element.text

    def wait_for_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))
    