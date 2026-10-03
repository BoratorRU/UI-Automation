from pages.login_page import LoginPage

def test_successful_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    
    # Авторизуемся под валидным пользователем
    login_page.login_with("standard_user", "secret_sauce")
    
    # Проверяем, что перешли на страницу с товарами
    assert "inventory.html" in driver.current_url, "Переход на страницу товаров не выполнен"

def test_failed_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    
    # Логинимся с неверным паролем
    login_page.login_with("standard_user", "wrong_password")
    
    # Проверяем появление сообщения об ошибке
    error_text = login_page.get_error_message()
    assert "Username and password do not match" in error_text, "Ошибка авторизации не появилась"
