import pytest
from utils.driver_factory import DriverFactory
from utils.config_reader import ConfigReader
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from utils.test_reporter import TestReporter


class TestAddToCart:
    """Test: search for a non-sold-out product, add it to cart, and verify."""

    @pytest.fixture(autouse=True)
    def setup(self, request):
        self.config = ConfigReader.get_config()
        self.driver = DriverFactory.get_driver("chrome")

        self.login_page = LoginPage(self.driver)
        self.products_page = ProductsPage(self.driver)
        self.cart_page = CartPage(self.driver)
        
        # Initialize Custom JSON Reporter
        self.reporter = TestReporter("Search for a product and add it to the cart")

        self.driver.get(self.config["base_url"])

        yield

        if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
            screenshot_path = f"screenshot_{request.node.name}.png"
            self.driver.save_screenshot(screenshot_path)
            print(f"\nScreenshot saved to {screenshot_path}")
            self.reporter.log_step("Test Failure", "FAIL", f"Screenshot saved at {screenshot_path}")
            self.reporter.finalize_report("FAIL")
        else:
            self.reporter.finalize_report("PASS")

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
        try:
            # 1. Login
            self.login_page.login(self.config["password"])
            self.reporter.log_step("Login", "PASS", "Logged in successfully.")

            # 2. Navigate to catalog and find the first available product
            self.products_page.navigate_to_catalog()
            product_name = self.products_page.find_first_available_product()
            self.reporter.log_step("Find Product", "PASS", f"Found product: '{product_name}'")

            # 3. Search for the product
            self.products_page.search_for_product(product_name)
            self.reporter.log_step("Search Product", "PASS", f"Searched for: '{product_name}'")

            # 4. Verify the product appears in search results
            result_names = self.products_page.get_search_result_names()
            assert any(product_name.lower() in r.lower() for r in result_names), \
                f"'{product_name}' not found in search results: {result_names}"
            self.reporter.log_step("Verify Search Results", "PASS", "Product found in search results.")

            # 5. Click the matching search result
            self.products_page.click_search_result(product_name)
            self.reporter.log_step("Open PDP", "PASS", "Clicked product to open PDP.")

            # 6. Verify PDP heading
            heading = self.products_page.get_product_heading()
            assert product_name.lower() in heading.lower(), \
                f"Expected heading '{product_name}', got '{heading}'"
            self.reporter.log_step("Verify PDP", "PASS", f"PDP heading matches: '{heading}'")

            # 7. Add to cart and verify badge shows 1
            self.cart_page.add_to_cart()
            badge = self.cart_page.get_cart_badge_count()
            assert badge == "1", f"Expected badge '1', got '{badge}'"
            self.reporter.log_step("Add to Cart", "PASS", "Product added to cart, badge updated to 1.")

            # 8. Open cart page and verify the correct product is listed
            self.cart_page.open_cart_page()
            cart_item = self.cart_page.get_cart_item_name()
            assert product_name.lower() in cart_item.lower(), \
                f"Expected '{product_name}' in cart, found '{cart_item}'"
            self.reporter.log_step("Verify Cart", "PASS", f"Product '{cart_item}' verified in cart.")

            print(f"\nTest passed: '{product_name}' added to cart and verified.")
        except Exception as e:
            self.reporter.log_step("Test Error", "FAIL", str(e))
            raise e
