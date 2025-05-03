import curl
import data
import locators


from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestRegistration:
        # Проверяем успешную регистрацию
    def test_registration_with_test_login(self, driver):
        # кликаем кнопку "Войти в аккаунт"
        driver.find_element(*locators.Locators.LOGIN_TO_ACCOUNT_BUTTON).click()
        
        # кликаем ссылку "Зарегистрироваться"
        driver.find_element(*locators.Locators.REG_PAGE_LINK).click()

        # заполнить обязательные поля для регистрации (имя, Email, пароль)
        driver.find_element(*locators.Locators.REG_NAME_FIELD).send_keys(data.Credentials.random_name)
        driver.find_element(*locators.Locators.REG_EMAIL_FIELD).send_keys(data.Credentials.random_email)
        driver.find_element(*locators.Locators.REG_PASSWORD_FIELD).send_keys(data.Credentials.random_password)
        
        # кликаем кнопку "Зарегистрироваться"
        driver.find_element(*locators.Locators.REG_NEW_ACCOUNT_BUTTON).click()

        # ожидание перехода на страницу формы входа
        WebDriverWait(driver, 10).until(EC.url_to_be(curl.LOGIN))

        # ввести данные зарегистрированного пользователя (Email, пароль)
        driver.find_element(*locators.Locators.LOGIN_EMAIL_FIELD).send_keys(data.Credentials.random_email)
        driver.find_element(*locators.Locators.LOGIN_PASSWORD_FIELD).send_keys(data.Credentials.random_password)

        # кликаем кнопку "Войти"
        driver.find_element(*locators.Locators.LOGIN_BUTTON).click()

        # ожидание перехода на главную страницу
        WebDriverWait(driver, 10).until(EC.url_to_be(curl.MAIN))
        
        # кликаем кнопку "Личный Кабинет"
        driver.find_element(*locators.Locators.PERSONAL_ACCOUNT_BUTTON).click()
    
        # ожидание перехода в Личный Кабинет
        WebDriverWait(driver, 10).until(EC.url_to_be(curl.PROFILE))
        
        # проверяем, что имя пользователя при регистрации совпадает с именем пользователя при входе в личный кабинет
        assert driver.find_element(*locators.Locators.NAME_SPACE).get_attribute("value") == data.Credentials.random_name, (
           "Имя пользователя при регистрации не равно имени пользователя в личном кабинете после входа")

        # Проверяем, что поле «Имя» должно быть не пустым
    def test_registration_with_empty_name(self, driver):
        # кликаем кнопку "Войти в аккаунт"
        driver.find_element(*locators.Locators.LOGIN_TO_ACCOUNT_BUTTON).click()
        
        # кликаем ссылку "Зарегистрироваться"
        driver.find_element(*locators.Locators.REG_PAGE_LINK).click()

        # заполнить обязательные поля для регистрации (имя оставляем не заполненным, Email, пароль)
        driver.find_element(*locators.Locators.REG_NAME_FIELD).send_keys(data.Credentials.empty_name)
        driver.find_element(*locators.Locators.REG_EMAIL_FIELD).send_keys(data.Credentials.random_email)
        driver.find_element(*locators.Locators.REG_PASSWORD_FIELD).send_keys(data.Credentials.random_password)

        # кликаем кнопку "Зарегистрироваться"
        driver.find_element(*locators.Locators.REG_NEW_ACCOUNT_BUTTON).click()
        name_spase = driver.find_element(*locators.Locators.REG_NAME_FIELD).get_attribute("value")

        # проверяем, что нельзя зарегистрироваться с пустым именем
        assert driver.current_url == curl.REGISTER and name_spase == "", \
            "Удалось зарегистрироваться с пустым именем"

        # Проверяем, что минимальный пароль — шесть символов
    def test_registration_with_invalid_password(self, driver):
        # кликаем кнопку "Войти в аккаунт"
        driver.find_element(*locators.Locators.LOGIN_TO_ACCOUNT_BUTTON).click()
        
        # кликаем ссылку "Зарегистрироваться"
        driver.find_element(*locators.Locators.REG_PAGE_LINK).click()
        
        # заполнить обязательные поля для регистрации (имя, Email, пароль меньше 6 символов)
        driver.find_element(*locators.Locators.REG_NAME_FIELD).send_keys(data.Credentials.random_name)
        driver.find_element(*locators.Locators.REG_EMAIL_FIELD).send_keys(data.Credentials.random_email)
        driver.find_element(*locators.Locators.REG_PASSWORD_FIELD).send_keys(data.Credentials.wrong_password)

        # кликаем кнопку "Зарегистрироваться"
        driver.find_element(*locators.Locators.REG_NEW_ACCOUNT_BUTTON).click()

        # проверяем, что нельзя зарегистрироваться с паролем меньше 6 символов и появляется сообщение об ошибка
        assert driver.find_element(*locators.Locators.INVALID_PASSWORD_MESSAGE).is_displayed(), \
            "Сообщение об ошибке 'Некорректный пароль', не отображается"