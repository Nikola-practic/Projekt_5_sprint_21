import locators

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestActivElementToConstructor:

        # Проверяем работу переход к разделу «Булки»
    def test_rolls_section_activation(self, driver):
        # кликаем по разделу "Конструктор"
        driver.find_element(*locators.Locators.TO_MAIN_BY_CONSTRUCTOR).click()

        # проверяем, что раздел "Булки" активен
        rolls_active_tab = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locators.Locators.ROLLS_ELEMENT_ACTIVE))
        assert rolls_active_tab.is_displayed(), "Элемент 'Булки' не стал активным"

        # Проверяем работу переход к разделу «Соусы»
    def test_sauces_section_activation(self, driver):
        # кликаем по разделу "Конструктор"
        driver.find_element(*locators.Locators.TO_MAIN_BY_CONSTRUCTOR).click()

        # кликаем по разделу "Соусы"
        driver.find_element(*locators.Locators.SAUCES_ELEMENT).click()
        
        # проверяем, что раздел "Соусы" стал активным
        sauces_active_tab = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locators.Locators.SAUCES_ELEMENT_ACTIVE))
        assert sauces_active_tab.is_displayed(), "Элемент 'Соусы' не стал активным"

        # Проверяем работу переход к разделу «Начинки»
    def test_toppings_section_activation(self, driver):
        # кликаем по разделу "Конструктор"
        driver.find_element(*locators.Locators.TO_MAIN_BY_CONSTRUCTOR).click()

        # кликаем по разделу "Начинки"
        driver.find_element(*locators.Locators.TOPPINGS_ELEMENT).click()

        # проверяем, что раздел "Начинки" стал активным
        toppings_active_tab = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locators.Locators.TOPPINGS_ELEMENT_ACTIVE))
        assert toppings_active_tab.is_displayed(), "Элемент 'Начинки' не стал активным"


    