def test_page_load(driver):
    driver.get("https://tetrisgame-samurajsam.netlify.app/")
    assert "tetris" in driver.page_source.lower(), "Strona Tetris nie załadowała się poprawnie"