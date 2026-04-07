import pytest
from utils.driver_factory import DriverFactory
from utils.config_reader import ConfigReader
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


class TestAddToCart:
    """Test: search for a non-sold-out product, add it to cart, and verify."""

    @pytest.fixture(autouse=True)
    def setup(self, request):
        self.config = ConfigReader.get_config()
        self.driver = DriverFactory.get_driver("chrome")

        self.login_page = LoginPage(self.driver)
        self.products_page = ProductsPage(self.driver)
        self.cart_page = CartPage(self.driver)

        self.driver.get(self.config["base_url"])

        yield

        if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
            screenshot_path = f"screenshot_{request.node.name}.png"
            self.driver.save_screenshot(screenshot_path)
            print(f"\nScreenshot saved to {screenshot_path}")

        self.driver.quit()

    def test_search_and_add_to_cart(self):
        """
        1. Login
        2. Go to catalog, find the first non-sold-out product name
        3. Search for that product using the search bar
        4. Verify search results contain the product
        5. Click the search result to open the PDP
        6. Verify the PDP heading matches
        7. Add to cart, verify badge count is 1
        8. Open the cart page, verify the product name appears
        """
        # 1. Login
        self.login_page.login(self.config["password"])

        # 2. Navigate to catalog and find the first available product
        self.products_page.navigate_to_catalog()
        product_name = self.products_page.find_first_available_product()
        print(f"\nFirst available product: '{product_name}'")

        # 3. Search for the product
        self.products_page.search_for_product(product_name)

        # 4. Verify the product appears in search results
        result_names = self.products_page.get_search_result_names()
        assert any(product_name.lower() in r.lower() for r in result_names), \
            f"'{product_name}' not found in search results: {result_names}"

        # 5. Click the matching search result
        self.products_page.click_search_result(product_name)

        # 6. Verify PDP heading
        heading = self.products_page.get_product_heading()
        assert product_name.lower() in heading.lower(), \
            f"Expected heading '{product_name}', got '{heading}'"

        # 7. Add to cart and verify badge shows 1
        self.cart_page.add_to_cart()
        badge = self.cart_page.get_cart_badge_count()
        assert badge == "1", f"Expected badge '1', got '{badge}'"

        # 8. Open cart page and verify the correct product is listed
        self.cart_page.open_cart_page()
        cart_item = self.cart_page.get_cart_item_name()
        assert product_name.lower() in cart_item.lower(), \
            f"Expected '{product_name}' in cart, found '{cart_item}'"

        print(f"\nTest passed: '{product_name}' added to cart and verified.")
