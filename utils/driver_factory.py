from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class DriverFactory:
    """Factory class to create WebDriver instances."""

    @staticmethod
    def get_driver(browser_type="chrome"):
        """:return: WebDriver instance """
        if browser_type.lower() == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            # options.add_argument("--headless=new")
            options.add_argument("--window-size=1920,1080")
            
            # Use ChromeDriverManager to automatically manage the driver executable
            driver = webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install()), 
                options=options
            )
            return driver
        else:
            raise ValueError(f"Browser type '{browser_type}' is not supported.")
