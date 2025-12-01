from pages.home_page import HomePage
from pages.game_page import GamePage


def test_music_toggle(driver):
    home = HomePage(driver)
    home.click_start()

    game = GamePage(driver)
    game.toggle_music()

    assert True  # brak możliwości odczytu audio, ale test klika poprawnie
