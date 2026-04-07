from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        """Initializes the Page Object"""
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def find_element(self, locator, timeout=10):
        """Waits for an element to be visible and returns it"""
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(locator))

    def click_element(self, locator, timeout=10):
        """Waits for an element to be clickable and performs a click"""
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def type_text(self, locator, text):
        """ Waits for an element to be visible and sends keys to it"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_title(self):
        """Returns the current page title"""
        return self.driver.title

    def get_url(self):
        """Returns the current URL"""
        return self.driver.current_url
