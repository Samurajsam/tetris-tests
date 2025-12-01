import pytest
from utils.driver_factory import create_driver
import config
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
