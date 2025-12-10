import pytest
from utils.driver_factory import create_driver
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
    # jest to "yield" które pozwala pytest działać dalej
    outcome = yield
    result = outcome.get_result()

    # robimy screen TYLKO przy failu
    if result.failed and "driver" in item.fixturenames:
        driver = item.funcargs["driver"]

        # katalog na screenshoty
        os.makedirs("screenshots", exist_ok=True)

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        test_name = item.name.replace("/", "_")
        filename = f"screenshots/{test_name}_{timestamp}.png"

        driver.save_screenshot(filename)

        # dodajemy screenshot do raportu GitHub Actions jako artefakt
        if os.getenv("GITHUB_ACTIONS") == "true":
            print(f"::warning file={filename},line=1,col=1::Screenshot saved: {filename}")
