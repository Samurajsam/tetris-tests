import pytest
from pages.home_page import HomePage
from pages.game_page import GamePage
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
import time

@pytest.mark.regression
@pytest.mark.game_state
def test_play_again(driver):
    home = HomePage(driver)
    home.click_start()

    game = GamePage(driver)

    # Wymuszamy szybki Game Over przez wielokrotne dropy
    # Gdy pojawi się Game Over, przycisk zniknie i dostaniemy wyjątek
    try:
        for _ in range(75):
            game.drop()
    except (TimeoutException, StaleElementReferenceException):
        pass

    game.wait_for_game_over()
    game.wait_for_condition(lambda: True, timeout=0.4)
    game.play_again()
    game.wait_for_condition(lambda: True, timeout=0.4)
    home.click_start()
    game.wait_for_condition(lambda: True, timeout=0.4)

    assert game.get_filled_count() > 0, "Gra nie rozpoczęła się ponownie po Game Over"

