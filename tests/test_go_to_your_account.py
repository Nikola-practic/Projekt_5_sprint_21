import curl
import data
import locators

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class TestMovingToPersonalAccount:

        # Проверяем переход по клику на «Личный кабинет»
    def test_click_on_personal_account(self, driver):
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

        # кликаем кнопку "Личный Кабинет"
        driver.find_element(*locators.Locators.PERSONAL_ACCOUNT_BUTTON).click()

        # ожидание перехода в личный кабинет
        WebDriverWait(driver, 10).until(EC.url_to_be(curl.PROFILE))

        # проверяем, что осуществлён вход в личный кабинет
        assert driver.current_url == curl.PROFILE, f"Ожидался URL {curl.PROFILE}, но получен {driver.current_url}"

        # Проверяем переход из личного кабинета по клику на «Конструктор»
    def test_from_profile_by_constructor(self, driver):
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

        # кликаем кнопку "Личный Кабинет"
        driver.find_element(*locators.Locators.PERSONAL_ACCOUNT_BUTTON).click()

        # ожидание перехода в личный кабинет
        WebDriverWait(driver, 10).until(EC.url_to_be(curl.PROFILE))
        
        # переходим на главную страницу через "Конструктор"
        driver.find_element(*locators.Locators.TO_MAIN_BY_CONSTRUCTOR).click()
        
        # ожидание перехода на главную страницу
        WebDriverWait(driver, 10).until(EC.url_to_be(curl.MAIN))

        # проверяем, что осуществлён переход на главную страницу
        assert driver.current_url == curl.MAIN, f"Ожидался URL {curl.MAIN}, но получен {driver.current_url}"

        # Проверяем переход из личного кабинета по клику на логотип Stellar Burgers
    def test_from_profile_by_logo(self, driver):
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

        # кликаем кнопку "Личный Кабинет"
        driver.find_element(*locators.Locators.PERSONAL_ACCOUNT_BUTTON).click()

        # ожидание перехода в личный кабинет
        WebDriverWait(driver, 10).until(EC.url_to_be(curl.PROFILE))

        # переход на главную страницу через логотип "Stellar Burgers"
        driver.find_element(*locators.Locators.TO_MAIN_BY_LOGO).click()
        
        # ожидание перехода на главную страницу
        WebDriverWait(driver, 10).until(EC.url_to_be(curl.MAIN))

        # проверяем, что осуществлён переход на главную страницу
        assert driver.current_url == curl.MAIN, f"Ожидался URL {curl.MAIN}, но получен {driver.current_url}"