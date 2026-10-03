from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://saucedemo.com"

    def open(self):
        self.driver.get(self.url)

    def find_element(self, locator, time=10):
        # Явное ожидание элемента (защита от моргающих тестов)
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Не удалось найти элемент по локатору {locator}"
        )

    def input_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def click_element(self, locator):
        self.find_element(locator).click()
