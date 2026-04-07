from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Page Object for the Shopify password-protected storefront."""

    __password_input_field = (By.ID, "password")
    __password_submit_button = (By.CSS_SELECTOR, "button[type='submit']")

    def __init__(self, driver):
        super().__init__(driver)

    def enter_password(self, password):
        """Types the store password into the input field."""
        self.type_text(self.__password_input_field, password)

    def click_submit(self):
        """Clicks the submit button on the password form."""
        self.click_element(self.__password_submit_button)

    def login(self, password):
        """Enters the store password and submits the form."""
        self.enter_password(password)
        self.click_submit()
