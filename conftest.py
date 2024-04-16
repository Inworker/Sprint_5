import pytest
from selenium import webdriver
import settings
from data import BurgerTestData
from locators import BurgerLocator


@pytest.fixture(scope="function")
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get(settings.URL)
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture(scope="function")
def page_forgot_password(driver):
    driver.get(settings.URL + 'forgot-password')
    driver.find_element(*BurgerLocator.BUTTON_LOGIN_FROM_FORGOT_PAGE).click()


@pytest.fixture(scope="function")
def send_data_pole_email(driver):
    email_input = driver.find_element(*BurgerLocator.INPUT_EMAIL)
    email_input.send_keys(*BurgerTestData.AUTH_EMAIL_CONST)


@pytest.fixture(scope="function")
def send_data_pole_password(driver):
    password_input = driver.find_element(*BurgerLocator.INPUT_PASSWORD)
    password_input.send_keys(*BurgerTestData.AUTH_PASSWORD_CONST)


@pytest.fixture(scope="function")
def button_enter(driver):
    button_login = driver.find_element(*BurgerLocator.BUTTON_ENTER)
    button_login.click()


@pytest.fixture(scope="function")
def page_register(driver):
    driver.get(settings.URL + 'register')


@pytest.fixture(scope="function")
def button_small_enter(driver):
    button_registration = driver.find_element(*BurgerLocator.BUTTON_SMALL_ENTER)
    button_registration.click()


@pytest.fixture(scope="function")
def start_page_login(driver):
    driver.find_element(*BurgerLocator.BUTTON_LOGIN).click()


@pytest.fixture(scope="function")
def start_page_profile(driver):
    driver.find_element(*BurgerLocator.BUTTON_ACCOUNT).click()


@pytest.fixture(scope="function")
def page_register(driver):
    driver.get(settings.URL + 'register')


@pytest.fixture(scope="function")
def input_name(driver):
    name_input = driver.find_element(*BurgerLocator.INPUT_NAME)
    name_input.send_keys(*BurgerTestData.AUTH_NAME)


@pytest.fixture(scope="function")
def good_password(driver):
    password_input = driver.find_element(*BurgerLocator.INPUT_PASSWORD)
    password_input.send_keys(*BurgerTestData.AUTH_PASSWORD)


@pytest.fixture(scope="function")
def bad_password(driver):
    password_input = driver.find_element(*BurgerLocator.INPUT_PASSWORD)
    password_input.send_keys(*BurgerTestData.BAD_AUTH_PASSWORD)


@pytest.fixture(scope="function")
def email_input_register(driver):
    email_input = driver.find_element(*BurgerLocator.INPUT_EMAIL)
    email_input.send_keys(*BurgerTestData.AUTH_EMAIL)


@pytest.fixture(scope="function")
def button_register(driver):
    button_registration = driver.find_element(*BurgerLocator.BUTTON_REGISTRATION)
    button_registration.click()
