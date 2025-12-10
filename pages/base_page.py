from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    def wait_for_condition(self, condition, timeout=10):
        """Czeka aż warunek (funkcja zwracająca bool) będzie True"""
        return WebDriverWait(self.driver, timeout).until(lambda driver: condition())

    def is_visible(self, locator):
        try:
            el = self.wait.until(EC.visibility_of_element_located(locator))
            return el.is_displayed()
        except:
            return False

    def exists(self, locator):
        return len(self.driver.find_elements(*locator)) > 0
