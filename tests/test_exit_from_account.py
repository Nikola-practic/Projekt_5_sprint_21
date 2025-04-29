import curl
import data
import locators

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestExit:
        # Проверяем выход по кнопке «Выйти» в личном кабинете
    def test_exit_from_account(self, driver):
        # кликаем кнопку "Личный Кабинет"
        driver.find_element(*locators.Locators.PERSONAL_ACCOUNT_BUTTON).click()

        # ожидание перехода на страницу формы входа
        WebDriverWait(driver, 10).until(EC.url_to_be(curl.LOGIN))

        # ввести данные зарегистрированного пользователя (mail, пароль)
        driver.find_element(*locators.Locators.LOGIN_EMAIL_FIELD).send_keys(data.Credentials.email)
        driver.find_element(*locators.Locators.LOGIN_PASSWORD_FIELD).send_keys(data.Credentials.password)

        # кликаем кнопку "Войти"
        driver.find_element(*locators.Locators.LOGIN_BUTTON).click()

        # ожидание перехода на основную страницу
        WebDriverWait(driver, 10).until(EC.url_to_be(curl.MAIN))

        # кликаем кнопку "Личный Кабинет"
        driver.find_element(*locators.Locators.PERSONAL_ACCOUNT_BUTTON).click()

        # ожидание перехода в личный кабинет
        WebDriverWait(driver, 10).until(EC.url_to_be(curl.PROFILE))

        # кликаем кнопку "Выход"
        driver.find_element(*locators.Locators.LOGOUT_BUTTON).click()

        # ожидание выхода из личного кабинета
        WebDriverWait(driver, 10).until(EC.url_to_be(curl.LOGIN))

        # проверяем переход на страницу формы входа
        assert driver.current_url == curl.LOGIN, f"Ожидался URL {curl.LOGIN}, но получен {driver.current_url}"