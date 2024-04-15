from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import BurgerLocator


class Test_Burger_Register:

    def test_successful_registration(self, driver, page_register, input_name, good_password, email_button_register):
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((BurgerLocator.TITLE_LOGIN)))
        Login = driver.find_element(*BurgerLocator.TITLE_LOGIN)
        assert Login.text == "Вход"
        driver.quit()

    def test_unsuccessful_registration_ucorrect_number(self, driver, page_register, input_name, bad_password,
                                                       email_button_register):
        title_error_password = driver.find_element(*BurgerLocator.TITLE_BAD_PASSWORD)
        assert title_error_password.is_displayed() and title_error_password.text == "Некорректный пароль"
        driver.quit()
