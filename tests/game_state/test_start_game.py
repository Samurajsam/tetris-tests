import pytest
from pages.home_page import HomePage
from pages.game_page import GamePage

@pytest.mark.smoke
@pytest.mark.game_state
def test_start_game(driver):
    home = HomePage(driver)
    home.click_start()

    game = GamePage(driver)
    assert game.get_filled_count() > 0, "Gra nie wystartowała - brak klocków na planszy"
