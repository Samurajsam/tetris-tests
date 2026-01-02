import pytest
from utils.driver_factory import create_driver
import allure
import config
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from datetime import datetime


@pytest.fixture
def driver():
    driver = create_driver(config.BROWSER)
    driver.set_window_size(1100, 900)
    driver.get(config.BASE_URL)

    # czekam na załadowanie strony i przycisku start
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class='start-btn']"))
    )

    yield driver
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.failed and "driver" in item.fixturenames:
        driver = item.funcargs["driver"]

        os.makedirs("screenshots", exist_ok=True)

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"screenshots/{item.name}_{timestamp}.png"

        driver.save_screenshot(filename)

        # 🔥 KLUCZOWE – załączenie do Allure
        with open(filename, "rb") as image:
            allure.attach(
                image.read(),
                name="Screenshot on failure",
                attachment_type=allure.attachment_type.PNG
            )
