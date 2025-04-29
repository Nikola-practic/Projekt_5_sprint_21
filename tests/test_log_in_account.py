import curl 
import data
import locators

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLoginTheSite:
        # Проверяем вход по кнопке «Войти в аккаунт» на главной
    def test_login_to_account_with_button_in_the_main_page(self, driver):
        # кликаем кнопку "Войти в аккаунт"
        driver.find_element(*locators.Locators.LOGIN_TO_ACCOUNT_BUTTON).click()

        # ожидание перехода на страницу формы входа
        WebDriverWait(driver, 10).until(EC.url_to_be(curl.LOGIN))

        # ввести данные зарегистрированного пользователя (mail, пароль)
        driver.find_element(*locators.Locators.LOGIN_EMAIL_FIELD).send_keys(data.Credentials.email)
        driver.find_element(*locators.Locators.LOGIN_PASSWORD_FIELD).send_keys(data.Credentials.password)

        # кликаем кнопку "Войти"
        driver.find_element(*locators.Locators.LOGIN_BUTTON).click()

        # ожидание перехода на главную страницу
        WebDriverWait(driver, 10).until(EC.url_to_be(curl.MAIN))

        # проверяем, что осуществлён переход на главную страницу
        assert driver.current_url == curl.MAIN, f"Ожидался URL {curl.MAIN}, но получен {driver.current_url}"

        # Проверяем вход через кнопку «Личный кабинет»
    def test_login_through_personal_account_button(self, driver):
        # кликаем кнопку "Личный Кабинет"
        driver.find_element(*locators.Locators.PERSONAL_ACCOUNT_BUTTON).click()

        # ожидание перехода на страницу формы входа
        WebDriverWait(driver, 10).until(EC.url_to_be(curl.LOGIN))

        # ввести данные зарегистрированного пользователя (mail, пароль)
        driver.find_element(*locators.Locators.LOGIN_EMAIL_FIELD).send_keys(data.Credentials.email)
        driver.find_element(*locators.Locators.LOGIN_PASSWORD_FIELD).send_keys(data.Credentials.password)

        # кликаем кнопку "Войти"
        driver.find_element(*locators.Locators.LOGIN_BUTTON).click()

        # ожидание перехода на главную страницу
        WebDriverWait(driver, 10).until(EC.url_to_be(curl.MAIN))

        # проверяем, что осуществлён переход на главную страницу
        assert driver.current_url == curl.MAIN, f"Ожидался URL {curl.MAIN}, но получен {driver.current_url}"

        # Проверяем вход через кнопку в форме регистрации
    def test_registration_with_test_login(self, driver):
        # кликаем кнопку "Войти в аккаунт"
        driver.find_element(*locators.Locators.LOGIN_TO_ACCOUNT_BUTTON).click()

        # ожидание перехода на страницу формы входа
        WebDriverWait(driver, 10).until(EC.url_to_be(curl.LOGIN))

        # кликаем ссылку "Зарегистрироваться"
        driver.find_element(*locators.Locators.REG_PAGE_LINK).click()

        # кликаем ссылку "Войти"
        driver.find_element(*locators.Locators.LOGIN_PAGE_LINK).click()

        # ожидание перехода на страницу формы входа
        WebDriverWait(driver, 10).until(EC.url_to_be(curl.LOGIN))

        # ввести данные зарегистрированного пользователя (mail, пароль)
        driver.find_element(*locators.Locators.LOGIN_EMAIL_FIELD).send_keys(data.Credentials.email)
        driver.find_element(*locators.Locators.LOGIN_PASSWORD_FIELD).send_keys(data.Credentials.password)

        # кликаем кнопку "Войти"
        driver.find_element(*locators.Locators.LOGIN_BUTTON).click()

        # ожидание перехода на главную страницу
        WebDriverWait(driver, 10).until(EC.url_to_be(curl.MAIN))

        # проверяем, что осуществлён переход на главную страницу
        assert driver.current_url == curl.MAIN, f"Ожидался URL {curl.MAIN}, но получен {driver.current_url}"

        # Проверяем вход через кнопку в форме восстановления пароля
    def test_login_from_recovery_form(self, driver):
        # кликаем кнопку "Войти в аккаунт"
        driver.find_element(*locators.Locators.LOGIN_TO_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.url_to_be(curl.LOGIN))

        # кликаем ссылку "Восстановить пароль"
        driver.find_element(*locators.Locators.PASSWORD_RECOVERY_LINK).click()

        # ожидание перехода на страницу восстановления пароля
        WebDriverWait(driver, 10).until(EC.url_to_be(curl.RECOVERY))

        # кликаем ссылку "Войти"
        driver.find_element(*locators.Locators.LOGIN_PAGE_LINK).click()

        # ожидание перехода на страницу формы входа
        WebDriverWait(driver, 10).until(EC.url_to_be(curl.LOGIN))

        # ввести данные зарегистрированного пользователя (mail, пароль)
        driver.find_element(*locators.Locators.LOGIN_EMAIL_FIELD).send_keys(data.Credentials.email)
        driver.find_element(*locators.Locators.LOGIN_PASSWORD_FIELD).send_keys(data.Credentials.password)

        # кликаем кнопку "Войти"
        driver.find_element(*locators.Locators.LOGIN_BUTTON).click()

        # ожидание перехода на главную страницу
        WebDriverWait(driver, 10).until(EC.url_to_be(curl.MAIN))

        # проверяем, что осуществлён переход на главную страницу
        assert driver.current_url == curl.MAIN, f"Ожидался URL {curl.MAIN}, но получен {driver.current_url}"