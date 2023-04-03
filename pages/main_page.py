
import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


# class MainPage(BasePage):
#     locators = MainPageLocators()
#
#     @allure.step('regions_cookies')
#     def check_regions_cookies(self):
#         self.element_is_visible(self.locators.REGIONS_BUTTON).click()
#         self.element_is_visible(self.locators.COOKIE_BUTTON).click()