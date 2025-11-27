from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_controls(driver):
    driver.get("https://tetrisgame-samurajsam.netlify.app/")
    wait = WebDriverWait(driver, 10)

    # Start
    start_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='start-btn']")))
    start_btn.click()

    board = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".board")))

    before = board.screenshot_as_png

    # klikamy "move left"
    move_left_btn = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".control-btn.left")
    ))
    move_left_btn.click()

    time.sleep(0.4)
    after = board.screenshot_as_png

    assert before != after, "Ruch w lewo nie zadziałał."
