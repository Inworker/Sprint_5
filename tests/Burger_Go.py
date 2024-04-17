from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import BurgerLocator
from settings import URL


class TestGoTo:
    def test_go_constructor_from_profile_page(self, driver, start_page_login, send_data_pole_email, send_data_pole_password,button_enter , start_page_profile):

        driver.find_element(*BurgerLocator.BUTTON_CONSTRUCTOR).click()
        burger_logo = driver.find_element(*BurgerLocator.LOGO)
        assert driver.current_url == URL and burger_logo.is_displayed()


    def test_go_to_profile_from_start_page(self, driver, start_page_login, send_data_pole_email,send_data_pole_password,button_enter, start_page_profile):

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(BurgerLocator.TITLE_PROFILE))
        element = driver.find_element(*BurgerLocator.TITLE_PROFILE)
        assert element.text == 'Профиль'


    def test_go_to_sous(self, driver, start_page_login, send_data_pole_email,send_data_pole_password,button_enter):

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((BurgerLocator.BUTTON_ZAKAZ)))

        sous = driver.find_element(*BurgerLocator.TAB_SOUS)
        sous.click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(BurgerLocator.CURRENT_TAB_SOUCE))
        assert sous == driver.find_element(*BurgerLocator.CURRENT_TAB_SOUCE)

    def test_go_to_NACHINKA(self, driver, start_page_login, send_data_pole_email, send_data_pole_password,
                             button_enter):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((BurgerLocator.BUTTON_ZAKAZ)))

        nachinka = driver.find_element(*BurgerLocator.TAB_NACHINKA)
        nachinka.click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(BurgerLocator.CURRENT_TAB_NACHINKA))
        assert nachinka == driver.find_element(*BurgerLocator.CURRENT_TAB_NACHINKA)

    def test_go_to_bulka(self, driver, start_page_login, send_data_pole_email, send_data_pole_password, button_enter):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((BurgerLocator.BUTTON_ZAKAZ)))

        nachinka = driver.find_element(*BurgerLocator.TAB_NACHINKA)
        nachinka.click()

        bulka = driver.find_element(*BurgerLocator.TAB_BULKA)
        bulka.click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(BurgerLocator.CURRENT_TAB_BULKA))
        assert bulka == driver.find_element(*BurgerLocator.CURRENT_TAB_BULKA)
