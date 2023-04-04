import time

import allure

from pages.main_page import MainPage


@allure.suite('MainPage')
class TestMainPage:
    @allure.feature('LoginRegistrationForm')
    class TestLoginForm:
        @allure.title('login_page')
        def test_login_form(self, driver):
            login_page = MainPage(driver, 'https://unsplash.com/')
            login_page.open()
            result = login_page.login_form()
            assert result != True, 'Invalid email or password.'

        @allure.title('login_page')
        def test_reg_form(self, driver):
            reg_page = MainPage(driver, 'https://unsplash.com/')
            reg_page.open()
            result = reg_page.reg_form()
            assert result == True, 'ERROR REGISTRATION'

    @allure.feature('TestMenu')
    class TestMenu:
        def test_hi_menu(self, driver):
            hi_menu = MainPage(driver, 'https://unsplash.com/')
            hi_menu.open()
            href_link, current_url = hi_menu.get_hi_menu_list()
            print(href_link, current_url)
            # assert href_link == current_url, "the link is broken or url is incorrect"

