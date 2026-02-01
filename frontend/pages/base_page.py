from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


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

    def wait_for_find_elements(self, *locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)
    
    def accept_alert(self, timeout=5):
        try:
            alert = WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
            alert.accept()
        except TimeoutException:
            pass
    
    def type_text(self, locator, text):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)
