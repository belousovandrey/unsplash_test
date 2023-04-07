import time

import allure
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
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
        @allure.title('login_page')
        def test_hi_menu(self, driver):
            hi_menu = MainPage(driver, 'https://unsplash.com/')
            hi_menu.open()
            result = hi_menu.get_hi_menu_list()
            assert result == True, f'the link is broken or url is incorrect,{result}'

        @allure.title('login_page')
        def test_hi_right_menu(self, driver):
            hi_menu = MainPage(driver, 'https://unsplash.com/')
            hi_menu.open()
            result = hi_menu.get_hi_right_menu_list()
            assert result == True, f'the link is broken or url is incorrect,{result}'

        @allure.title('login_page')
        def test_unsplash_menu_list(self, driver):
            hi_menu = MainPage(driver, 'https://unsplash.com/')
            hi_menu.open()
            result = hi_menu.get_unsplash_menu_list()
            assert result == True, f'the link is broken or url is incorrect,{result}'

    @allure.feature('TestMenu')
    class TestBurger:

        @allure.title('login_page')
        def test_burger_company(self, driver):
            burger_company = MainPage(driver, 'https://unsplash.com/')
            burger_company.open()
            result = burger_company.get_burger_company()
            assert result == True, f'the link is broken or url is incorrect,{result}'

        @allure.title('login_page')
        def test_burger_product(self, driver):
            burger_product = MainPage(driver, 'https://unsplash.com/')
            burger_product.open()

            result = burger_product.get_burger_product()
            assert result == True, f'the link is broken or url is incorrect,{result}'

        # @allure.title('login_page')
        # def test_hi_menu(self, driver):
        #     hi_menu = MainPage(driver, 'https://unsplash.com/')
        #     hi_menu.open()
        #     result = hi_menu.get_hi_menu_list()
        #     assert result == True, f'the link is broken or url is incorrect,{result}'

