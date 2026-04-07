from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class CartPage(BasePage):
    """Page Object for add-to-cart actions and cart page verification."""

    __add_to_cart_button = (By.CSS_SELECTOR, "button.product-form__submit[name='add']")
    __cart_icon = (By.ID, "cart-icon-bubble")
    __cart_badge_label = (By.CSS_SELECTOR, ".cart-count-bubble span[aria-hidden='true']")
    __cart_item_name = (By.CSS_SELECTOR, "#MainContent a.cart-item__name")

    def __init__(self, driver):
        super().__init__(driver)

    def add_to_cart(self):
        """Clicks the Add to Cart button and waits for the badge to show '1'."""
        self.click_element(self.__add_to_cart_button)
        self.wait.until(
            EC.text_to_be_present_in_element(self.__cart_badge_label, "1")
        )

    def get_cart_badge_count(self):
        """Returns the cart badge count text, or '0' if the badge is absent."""
        try:
            element = self.find_element(self.__cart_badge_label, timeout=3)
            return element.text.strip()
        except Exception:
            return "0"

    def open_cart_page(self):
        """Navigates to the /cart page by reading the cart icon's href."""
        cart_link = self.find_element(self.__cart_icon)
        href = cart_link.get_attribute("href")
        self.driver.get(href)
        self.wait.until(EC.presence_of_element_located(self.__cart_item_name))

    def get_cart_item_name(self):
        """Returns the product name shown in the cart table."""
        return self.find_element(self.__cart_item_name).text.strip()
