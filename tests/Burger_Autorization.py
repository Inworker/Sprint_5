from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import BurgerLocator


class Test_Burger_Autorizstion:
    def test_autorization_from_page_forgot_password(self, driver, page_forgot_password, auth_user_page_forgot_password):
        WebDriverWait(driver, 1).until(expected_conditions.visibility_of_element_located((BurgerLocator.BUTTON_ZAKAZ)))
        element = driver.find_element(*BurgerLocator.BUTTON_ZAKAZ)
        assert element.text == 'Оформить заказ'
        driver.quit()

    def test_autorization_from_page_register(self, driver, page_register_password, auth_user_page):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((BurgerLocator.BUTTON_ZAKAZ)))
        element = driver.find_element(*BurgerLocator.BUTTON_ZAKAZ)
        assert element.text == 'Оформить заказ'
        driver.quit()

    def test_autorization_from_start_page_button_login(self, driver, start_page_login, auth_user_page):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((BurgerLocator.BUTTON_ZAKAZ)))
        element = driver.find_element(*BurgerLocator.BUTTON_ZAKAZ)
        assert element.text == 'Оформить заказ'
        driver.quit()

    def test_autorization_from_start_page_button_profile(self, driver, start_page_profile, auth_user_page):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((BurgerLocator.BUTTON_ZAKAZ)))
        element = driver.find_element(*BurgerLocator.BUTTON_ZAKAZ)
        assert element.text == 'Оформить заказ'
        driver.quit()
