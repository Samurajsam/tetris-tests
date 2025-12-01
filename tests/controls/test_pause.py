from pages.home_page import HomePage
from pages.game_page import GamePage
import time


def test_pause(driver):
    home = HomePage(driver)
    home.click_start()

    game = GamePage(driver)
    before = game.get_filled_count()

    time.sleep(0.5)
    game.pause()

    time.sleep(1)
    after = game.get_filled_count()

    assert before == after, "Gra powinna być zatrzymana!"
