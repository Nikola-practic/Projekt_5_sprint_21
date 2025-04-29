from selenium.webdriver.common.by import By


class Locators:
    # Кнопка "Войти в аккаунт"
    LOGIN_TO_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")
    
    # Ссылка на страницу регистрации "Зарегистрироваться"
    REG_PAGE_LINK = (By.XPATH, "//a[contains(text(), 'Зарегистрироваться')]")
    
    # Поле имя в форме регистрации
    REG_NAME_FIELD = (By.XPATH, "//*[@id='root']//input")
    
    # Поле email в форме регистрации
    REG_EMAIL_FIELD = (By.XPATH, "//form//fieldset[2]//input")
    
    # Поле пароль в форме регистрации
    REG_PASSWORD_FIELD = (By.XPATH, "//input[@name='Пароль']")
    
    # Кнопка регистрации в форме регистрации "Зарегистрироваться"
    REG_NEW_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    
    # Сообщение о не корректном пароле
    INVALID_PASSWORD_MESSAGE = (By.XPATH, "//p[@class='input__error text_type_main-default' and text()='Некорректный пароль']")

    # Поле имя в личном кабинете пользователя
    NAME_SPACE = (By.XPATH, "//input[@type='text' and @name='Name']")

    # Поле Email в форме входа
    LOGIN_EMAIL_FIELD = (By.XPATH, "//input[@type='text' and @name='name']")
    
    # Поле Пароль в форме входа
    LOGIN_PASSWORD_FIELD = (By.XPATH, "//input[@type='password']")

    # Кнопка "Войти" в форме входа
    LOGIN_BUTTON = (By.XPATH, '//button[text()="Войти"]')

    # Ссылка в форме регистрации "Войти" на страницу формы входа
    LOGIN_PAGE_LINK = (By.XPATH, "//a[@class='Auth_link__1fOlj' and text()='Войти']")

    # Кнопка "Личный Кабинет"
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")

    # Переход на главную страницу через "Конструктор"
    TO_MAIN_BY_CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']")

    # Переход на главную страницу через логотип "Stellar Burgers"
    TO_MAIN_BY_LOGO = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo__2D0X2')]")

    # Ссылка в форме входа "Восстановить пароль" на страницу восстановления пароля
    PASSWORD_RECOVERY_LINK = (By.XPATH, "//a[@class='Auth_link__1fOlj' and text()='Восстановить пароль']")
    
    # Кнопка "Выход" из личного кабинета
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")

    # Раздел "Булки"
    ROLLS_ELEMENT = (By.XPATH, "//span[text()='Булки']")
    
    # Активность раздела "Булки"
    ROLLS_ELEMENT_ACTIVE = (By.XPATH, "//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect' and span[text()='Булки']]")

    # Раздел "Соусы"
    SAUCES_ELEMENT = (By.XPATH, "//span[text()='Соусы']")
    
    # Активность раздела "Соусы"
    SAUCES_ELEMENT_ACTIVE = (By.XPATH, "//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect' and span[text()='Соусы']]")

    # Раздел "Начинки"
    TOPPINGS_ELEMENT = (By.XPATH, "//span[text()='Начинки']")
    
    # Активность раздела "Начинки"
    TOPPINGS_ELEMENT_ACTIVE = (By.XPATH, "//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect' and span[text()='Начинки']]")
