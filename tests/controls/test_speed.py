from pages.home_page import HomePage
from pages.game_page import GamePage


def test_speed_down(driver):
    home = HomePage(driver)
    home.click_start()

    game = GamePage(driver)
    before = game.get_filled_ids()

    game.speed_down()
    
    # Czekamy aż klocek spadnie (stan planszy się zmieni)
    game.wait_for_condition(lambda: game.get_filled_ids() != before, timeout=5)
    after = game.get_filled_ids()

    assert before != after, "Klocek nie przyśpiesza"
