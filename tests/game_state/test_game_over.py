from pages.home_page import HomePage
from pages.game_page import GamePage


def test_game_over(driver):
    home = HomePage(driver)
    home.click_start()

    game = GamePage(driver)

    # Wymuszamy szybki Game Over przez wielokrotne dropy
    for _ in range(75):
        game.drop()

    # Po Game Over pojawia się overlay z przyciskiem "Play Again"
    game_over_overlay = game.wait_for_game_over()

    assert game_over_overlay.is_displayed(), "Game Over nie nastąpił!"
