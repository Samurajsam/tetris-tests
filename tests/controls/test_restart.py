from pages.home_page import HomePage
from pages.game_page import GamePage


def test_restart(driver):
    home = HomePage(driver)
    home.click_start()

    game = GamePage(driver)
    before = game.get_filled_ids()

    game.restart()
    
    # Czekamy aż stan planszy się zmieni po restarcie
    game.wait_for_condition(lambda: game.get_filled_ids() != before, timeout=5)
    after = game.get_filled_ids()

    assert before != after or after > 0, "Restart nie zresetował gry"
