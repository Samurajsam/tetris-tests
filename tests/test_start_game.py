from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_start_game(driver):
    driver.get("https://tetrisgame-samurajsam.netlify.app/")
    wait = WebDriverWait(driver, 10)

    # Klikamy start
    start_btn = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@class='start-btn']")
    ))
    start_btn.click()

    # Czekamy aż pojawią się komórki planszy
    cells_before = wait.until(EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, ".board .cell")
    ))

    # screenshot DIV BOARD, nie canvasu!
    board = driver.find_element(By.CSS_SELECTOR, ".board")
    screenshot_before = board.screenshot_as_png

    # Czekamy aż gra zacznie animację (ok. 0.6 sek)
    time.sleep(0.6)

    screenshot_after = board.screenshot_as_png

    assert screenshot_before != screenshot_after, "Gra nie rozpoczęła animacji!"
