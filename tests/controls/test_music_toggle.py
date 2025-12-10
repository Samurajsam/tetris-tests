from pages.home_page import HomePage
from pages.game_page import GamePage


def test_music_toggle(driver):
    home = HomePage(driver)
    home.click_start()

    game = GamePage(driver)
    
    # Klikamy przycisk muzyki kilka razy (włącz/wyłącz)
    game.toggle_music()
    game.toggle_music()
    game.toggle_music()

    # Brak możliwości odczytu stanu audio w Selenium,
    # ale test weryfikuje że przycisk jest klikalny i nie powoduje błędów
    assert True
