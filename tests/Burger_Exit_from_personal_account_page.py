from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import BurgerLocator


class TestExitFromAccount:
    def test_exit_acc(self, driver, start_page_login, send_data_pole_email,send_data_pole_password, button_enter, start_page_profile):

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(BurgerLocator.TITLE_PROFILE))
        driver.find_element(*BurgerLocator.BUTTON_EXIT).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(BurgerLocator.TITLE_LOGIN))
        element = driver.find_element(*BurgerLocator.TITLE_LOGIN)
        assert element.text == 'Вход'

