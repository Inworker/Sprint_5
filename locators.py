from selenium.webdriver.common.by import By

class BurgerLocator:
    INPUT_NAME = (By.XPATH, "//label[text() = 'Имя']/../input")  #Форма регистрации.Поле ввода Имя
    INPUT_EMAIL = (By.XPATH, "//label[text() = 'Email']/../input") #Форма регистрации.Поле ввода Email
    INPUT_PASSWORD = (By.XPATH, "//label[text() = 'Пароль']/../input") #Форма регистрации.Поле ввода Пароль

    TITLE_LOGIN = (By.XPATH, '//h2[text()= "Вход"]') # Форма авторизации. Заголовок "Вход"
    TITLE_BAD_PASSWORD = (By.XPATH, "//p[text()='Некорректный пароль']") # Форма авторизации. Текст "Некорректный пароль"
    TITLE_PROFILE = (By.XPATH, "//a[text()='Профиль']") #Профиль пользователя. Заголовок раздела "Профиль"

    BUTTON_REGISTRATION = (By.XPATH,'.//button[text()="Зарегистрироваться"]') #Форма регистрации. Кнопка "Зарегистрироваться"
    BUTTON_ACCOUNT = (By.XPATH, "//a[@class='AppHeader_header__link__3D_hX' and @href='/account']") #Главная страница. ссылка на личный кабинет
    BUTTON_LOGIN_FROM_FORGOT_PAGE = (By.XPATH,'.//a[@href="/login"]') #Форма восстановления пароля. Ссылка "Войти"
    BUTTON_LOGIN = (By.XPATH, './/button[text()="Войти в аккаунт"]') #Главная страница. Кнопка "Войти в аккаунт"
    BUTTON_ZAKAZ = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]") #Главная страница авторизованного пользователя. кнопка "оформить заказ"
    BUTTON_ENTER = (By.XPATH, "//button[text()='Войти']")# Форма авторизации, кнопка "Войти" (в Айти =)
    BUTTON_SMALL_ENTER = (By.XPATH, "//a[@class='Auth_link__1fOlj' and @href='/login' and text()='Войти']") #Форма регистрации. Ссылка "Войти"
    BUTTON_EXIT = (By.XPATH, "//button[@type='button' and @class='Account_button__14Yp3 text text_type_main-medium text_color_inactive' and text()='Выход']") #Профиль пользователя.Кнопка "Выход"
    BUTTON_CONSTRUCTOR = (By.XPATH, "//a[@class='AppHeader_header__link__3D_hX' and @href='/']") #Главная страница. Иконка + ссылка на кноструктор

    LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2") #Логотип бургера
    TAB_SOUS = (By.XPATH, '//span[text() = "Соусы"]') #раздел "Соусы"
    TAB_NACHINKA = (By.XPATH, '//span[text() = "Начинки"]')#раздел "Начинки"
    TAB_BULKA = (By.XPATH, '//span[text() = "Булки"]')#раздел "Булки"

    CURRENT_TAB_SOUCE = (By.XPATH, ".//div[contains(@class,'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect')]/span[text()= 'Соусы']") #раздел "Соусы". выбран текущий раздел
    CURRENT_TAB_NACHINKA = (By.XPATH,".//div[contains(@class,'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect')]/span[text()= 'Начинки']") #раздел "Начинки". выбран текущий раздел
    CURRENT_TAB_BULKA = (By.XPATH, ".//div[contains(@class,'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect')]/span[text()= 'Булки']") #раздел "Булки". выбран текущий раздел