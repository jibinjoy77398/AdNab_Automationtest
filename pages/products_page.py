from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class ProductsPage(BasePage):
    """Page Object for product catalog, search, and product detail pages."""

    # Catalog locators
    __catalog_link = (By.LINK_TEXT, "Catalog")
    __product_cards = (By.CSS_SELECTOR, "li.grid__item")
    __product_title_link = (By.CSS_SELECTOR, ".card__heading a")
    __next_page_button = (By.CSS_SELECTOR, "a[aria-label='Next page']")

    # Search locators
    __search_icon = (By.CSS_SELECTOR, "details-modal > details > summary[aria-label='Search']")
    __search_input = (By.CSS_SELECTOR, "#Search-In-Modal")
    __search_results_links = (By.CSS_SELECTOR, "a.predictive-search__item--link-with-thumbnail")

    # Product detail page locators
    __product_heading = (By.CSS_SELECTOR, "h1.product__title, .product__title h1")

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_catalog(self):
        """Navigates to the /collections/all catalog page."""
        self.click_element(self.__catalog_link)
        self.wait.until(EC.presence_of_all_elements_located(self.__product_cards))

    def find_first_available_product(self):
        """
        It scans the pages and returns the name of the first product with an active 'Add to Cart' button
        """
        while True:
            cards = self.wait.until(
                EC.presence_of_all_elements_located(self.__product_cards)
            )

            for card in cards:
                card_text = card.text.lower()
                if "sold out" in card_text:
                    continue
                link = card.find_element(*self.__product_title_link)
                name = link.get_attribute("textContent").strip()
                if name:
                    return name

            # Try next page
            try:
                next_btn = self.driver.find_element(*self.__next_page_button)
                self.driver.execute_script("arguments[0].click();", next_btn)
                self.wait.until(EC.staleness_of(cards[0]))
            except Exception:
                break

        raise Exception("No available (non-sold-out) product found across all catalog pages.")

    def search_for_product(self, product_name):
        """Opens the search modal and types the product name."""
        self.click_element(self.__search_icon)
        search_input = self.find_element(self.__search_input)
        search_input.clear()
        search_input.send_keys(product_name)

    def get_search_result_names(self):
        """Returns the names of the suggested products in the search bar"""
        self.wait.until(
            EC.presence_of_all_elements_located(self.__search_results_links)
        )
        links = self.driver.find_elements(*self.__search_results_links)
        return [link.text.strip() for link in links if link.is_displayed()]

    def click_search_result(self, product_name):
        """Clicks the visible search result link that matches the given product name."""
        links = self.driver.find_elements(*self.__search_results_links)
        for link in links:
            if link.is_displayed() and product_name.lower() in link.text.strip().lower():
                self.driver.execute_script("arguments[0].click();", link)
                return
        raise Exception(f"Visible search result for '{product_name}' not found.")

    def get_product_heading(self):
        """Returns the h1 heading text on the product detail page."""
        return self.find_element(self.__product_heading).text.strip()
