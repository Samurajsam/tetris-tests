import time

from pages.home_page import HomePage
from pages.game_page import GamePage


def test_speed_down(driver):
    home = HomePage(driver)
    home.click_start()

    game = GamePage(driver)
    before = game.get_filled_ids()

    game.speed_down()
    time.sleep(0.4)
    after = game.get_filled_ids()

    assert before != after
