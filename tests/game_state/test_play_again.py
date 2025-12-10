from pages.home_page import HomePage
from pages.game_page import GamePage
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
import time


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
    time.sleep(0.4)
    game.play_again()
    time.sleep(0.4)
    home.click_start()
    time.sleep(0.4)

    assert game.get_filled_count() > 0, "Gra nie rozpoczęła się ponownie po Game Over"

