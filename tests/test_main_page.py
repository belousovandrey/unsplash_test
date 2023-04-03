import time

import allure
from pages.main_page import MainPage


@allure.suite('MainPage')
class TestMainPage:
    @allure.feature('LoginRegistrationForm')
    class TestLoginForm:
        @allure.title('login_page')
        def test_login_page(self, driver):
            login_page = MainPage(driver, 'https://gettzap.ru/')
            login_page.open()
            login_page.check_regions_cookies()