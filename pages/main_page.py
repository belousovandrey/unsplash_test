import time
import requests
import allure
from selenium.webdriver.common.by import By
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

    @allure.step('get_hi_menu_list')
    def get_hi_menu_list(self):
        for i in range(2, 20):
            simple_link = self.element_is_visible((By.CSS_SELECTOR,
                                                   f'#app > div > div.b4j4s > div > div > div.BK8tG > div > div.pRk2s > div.VCR4P > ul > li:nth-child({i}) > a'))
            link_href = simple_link.get_attribute('href')
            request = requests.get(link_href)
            if request.status_code == 200:
                simple_link.click()
                if i % 5 == 0:
                    self.element_is_visible(self.locators.MENU_RIGHT).click()
                self.driver.switch_to.window(self.driver.window_handles[1])
                url = self.driver.current_url
                if link_href != url:
                    return (link_href, request.status_code)
            else:
                return (link_href, request.status_code)
        return True
