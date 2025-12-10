from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class  HomePage(BasePage):
    START_BUTTON = (By.XPATH, "//button[@class='start-btn']")

    def click_start(self):
        self.click(self.START_BUTTON)
