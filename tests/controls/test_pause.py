import pytest
from pages.home_page import HomePage
from pages.game_page import GamePage
import time

@pytest.mark.regression
@pytest.mark.controls
def test_game_pause(driver):
    home = HomePage(driver)
    home.click_start()

    game = GamePage(driver)
    
    # Czekamy aż kilka klocków spadnie
    game.wait_for_condition(lambda: True, timeout=1)

    # Pauza (nieparzysta liczba kliknięć = gra zatrzymana)
    game.pause()
    
    # Czekamy chwilę żeby gra się zatrzymała
    game.wait_for_condition(lambda: True, timeout=0.5)
    
    # Zapisujemy stan PO zatrzymaniu gry
    before = game.get_filled_count()

    # Czekamy dłużej żeby upewnić się że gra jest zatrzymana
    game.wait_for_condition(lambda: True, timeout=3)
    after = game.get_filled_count()

    assert before == after, "Gra powinna być zatrzymana!"
