from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import BurgerLocator


class Test_exit_from_account:
    def test_exit_acc(self, driver, start_page_login, auth_user_page, start_page_profile):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(BurgerLocator.TITLE_PROFILE))
        driver.find_element(*BurgerLocator.BUTTON_EXIT).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(BurgerLocator.TITLE_LOGIN))
        element = driver.find_element(*BurgerLocator.TITLE_LOGIN)
        assert element.text == 'Вход'
        driver.quit()
