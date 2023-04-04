import time

import allure

from auth_data import *
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    locators = MainPageLocators()

    @allure.step('login_form')
    def login_form(self):
        self.element_is_visible(self.locators.LOG_IN_BUTTON).click()
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.LOGIN_BUTTON).click()
        result = self.element_is_not_present(self.locators.LOGIN_ERROR)
        return result

    @allure.step('reg_form')
    def reg_form(self):
        self.element_is_visible(self.locators.LOG_IN_BUTTON).click()
        self.go_to_element(self.element_is_visible(self.locators.REG_BUTTON))
        self.element_is_visible(self.locators.REG_BUTTON).click()
        self.element_is_visible(self.locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(self.locators.LAST_NAME).send_keys(last_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.USER_NAME).send_keys(user_name)
        self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        self.go_to_element(self.element_is_visible(self.locators.REG_FIN_BUTTON))
        self.element_is_visible(self.locators.REG_FIN_BUTTON).click()
        result = self.element_is_not_present(self.locators.GOOD_REG)
        return result
