import os

from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService


def _is_ci() -> bool:
    return os.getenv("CI", "").lower() in {"1", "true"} or os.getenv("GITHUB_ACTIONS") == "true"


def create_driver(browser_name: str = "firefox"):
    if browser_name == "firefox":
        options = FirefoxOptions()
        if _is_ci():
            options.add_argument("--headless")
        return webdriver.Firefox(options=options)

    if browser_name == "chrome":
        options = ChromeOptions()
        if _is_ci():
            options.add_argument("--headless=new")
        service = ChromeService()
        return webdriver.Chrome(service=service, options=options)

    raise ValueError(f"Unknown browser: {browser_name}")
