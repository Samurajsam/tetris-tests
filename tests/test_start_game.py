from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_start_game(driver):
    driver.get("https://tetrisgame-samurajsam.netlify.app/")
    body = driver.find_element(By.TAG_NAME, "body")

    body.send_keys(Keys.SPACE)
    time.sleep(1)

    canvas = driver.find_element(By.TAG_NAME, "canvas")
    before = canvas.screenshot_as_png

    time.sleep(0.5)
    after = canvas.screenshot_as_png

    assert before != after, "Gra się nie uruchomiła."