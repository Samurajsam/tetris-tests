from pages.home_page import HomePage
from pages.game_page import GamePage


def test_restart(driver):
    home = HomePage(driver)
    home.click_start()

    game = GamePage(driver)
    before = game.get_filled_count()

    game.restart()
    after = game.get_filled_count()

    assert before != after or after > 0
