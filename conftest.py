import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def driver():
    # Автоматически скачивает и запускает правильную версию Chrome
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized") # Открываем на весь экран
    
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit() # Закрываем браузер после теста
