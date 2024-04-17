from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import BurgerLocator


class TestBurgerAutorizstion:
    def test_autorization_from_page_forgot_password(self, driver, page_forgot_password,send_data_pole_email,send_data_pole_password, button_enter):
        WebDriverWait(driver, 1).until(expected_conditions.visibility_of_element_located((BurgerLocator.BUTTON_ZAKAZ)))
        element = driver.find_element(*BurgerLocator.BUTTON_ZAKAZ)
        assert element.text == 'Оформить заказ'

    def test_autorization_from_page_register(self, driver, page_register, button_small_enter, send_data_pole_email, send_data_pole_password,button_enter):

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((BurgerLocator.BUTTON_ZAKAZ)))
        element = driver.find_element(*BurgerLocator.BUTTON_ZAKAZ)
        assert element.text == 'Оформить заказ'


    def test_autorization_from_start_page_button_login(self, driver, start_page_login, send_data_pole_email, send_data_pole_password,button_enter):


        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((BurgerLocator.BUTTON_ZAKAZ)))
        element = driver.find_element(*BurgerLocator.BUTTON_ZAKAZ)
        assert element.text == 'Оформить заказ'


    def test_autorization_from_start_page_button_profile(self, driver, start_page_profile, send_data_pole_email, send_data_pole_password, button_enter):


        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((BurgerLocator.BUTTON_ZAKAZ)))
        element = driver.find_element(*BurgerLocator.BUTTON_ZAKAZ)
        assert element.text == 'Оформить заказ'

