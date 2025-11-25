from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_controls(driver):
    driver.get("https://tetrisgame-samurajsam.netlify.app/")
    body = driver.find_element(By.TAG_NAME, "body")

    # start
    body.send_keys(Keys.SPACE)
    time.sleep(0.5)

    canvas = driver.find_element(By.TAG_NAME, "canvas")

    before_move = canvas.screenshot_as_png
    body.send_keys(Keys.ARROW_LEFT)
    time.sleep(0.3)
    after_move = canvas.screenshot_as_png

    assert before_move != after_move, "Ruch w lewo nie zadziałał."