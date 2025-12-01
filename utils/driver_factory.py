from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager


def create_driver(browser_name="firefox"):
    if browser_name == "firefox":
        return webdriver.Firefox()

    if browser_name == "chrome":
        from selenium.webdriver.chrome.service import Service
        service = Service(ChromeDriverManager().install())
        return webdriver.Chrome(service=service)

    raise ValueError(f"Unknown browser: {browser_name}")
