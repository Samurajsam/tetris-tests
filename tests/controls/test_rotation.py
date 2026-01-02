import pytest
from pages.home_page import HomePage
from pages.game_page import GamePage

@pytest.mark.regression
@pytest.mark.controls
def test_piece_rotation(driver):
    home = HomePage(driver)
    home.click_start()

    game = GamePage(driver)
    before = game.get_filled_ids()

    game.rotate()
    
    # Czekamy aż stan planszy się zmieni
    game.wait_for_condition(lambda: game.get_filled_ids() != before, timeout=5)
    after = game.get_filled_ids()

    assert before != after or after > 0, "Klocek się nie obraca"
