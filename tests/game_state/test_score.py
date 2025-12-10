from pages.home_page import HomePage
from pages.game_page import GamePage


def test_score_display_on_start(driver):
    home = HomePage(driver)
    home.click_start()

    game = GamePage(driver)
    score = game.get_score()

    assert score == 0, "Początkowy wynik powinien wynosić 0"
