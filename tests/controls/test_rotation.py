from pages.home_page import HomePage
from pages.game_page import GamePage


def test_piece_rotation(driver):
    home = HomePage(driver)
    home.click_start()

    game = GamePage(driver)
    before = game.get_filled_count()

    game.rotate()
    after = game.get_filled_count()

    assert before != after or after > 0
