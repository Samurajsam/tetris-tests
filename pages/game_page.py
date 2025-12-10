from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time


class GamePage(BasePage):

    # przyciski
    ROTATE_BTN = (By.CSS_SELECTOR, ".btn-a")
    DROP_BTN = (By.CSS_SELECTOR, ".btn-b")
    LEFT_BTN = (By.CSS_SELECTOR, ".left")
    RIGHT_BTN = (By.CSS_SELECTOR, ".right")
    PAUSE_BTN = (By.CSS_SELECTOR, ".pause-btn")
    RESTART_BTN = (By.CSS_SELECTOR, ".restart-btn")
    MUSIC_BTN = (By.CSS_SELECTOR, ".music-toggle")

    # game over
    GAME_OVER_OVERLAY = (By.CSS_SELECTOR, ".gameover")
    PLAY_AGAIN_BTN = (By.CSS_SELECTOR, ".play-again-btn")

    # wynik
    SCORE = (By.CSS_SELECTOR, ".score")

    # plansza
    FILLED_CELLS = (By.CSS_SELECTOR, ".board .cell.filled")
    ALL_CELLS = (By.CSS_SELECTOR, ".board .cell")

    def get_filled_count(self):
        return len(self.find_all(self.FILLED_CELLS))

    def get_filled_ids(self):
        cells = self.find_all(self.ALL_CELLS)
        return {index for index, cell in enumerate(cells) if "filled" in cell.get_attribute("class")}

    def get_score(self):
        text = self.find(self.SCORE).text  # np. "Score: 0"
        digits = "".join(ch for ch in text if ch.isdigit())
        return int(digits) if digits else 0

    def rotate(self):
        self.click(self.ROTATE_BTN)
        time.sleep(0.2)

    def move_left(self):
        self.click(self.LEFT_BTN)
        time.sleep(0.2)

    def move_right(self):
        self.click(self.RIGHT_BTN)
        time.sleep(0.2)

    def drop(self):
        self.click(self.DROP_BTN)
        time.sleep(0.2)

    def pause(self):
        self.click(self.PAUSE_BTN)

    def restart(self):
        self.click(self.RESTART_BTN)

    def toggle_music(self):
        self.click(self.MUSIC_BTN)

    def speed_down(self, clicks=3):
        for _ in range(clicks):
            self.drop()

    def wait_for_game_over(self):
        return self.find(self.GAME_OVER_OVERLAY)

    def play_again(self):
        self.click(self.PLAY_AGAIN_BTN)
        time.sleep(0.2)
