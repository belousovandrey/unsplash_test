from datetime import time

import allure
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium import webdriver


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    @allure.step('Open a browser')
    def open(self):
        self.driver.get(self.url)

    @allure.step('element_is_visible')
    def element_is_visible(self, locator, timeout=5):
        self.go_to_element(self.element_is_present(locator))
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step('elements_are_visible')
    def elements_are_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    @allure.step('element_is_present')
    def element_is_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    @allure.step('elements_are_present')
    def elements_are_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    @allure.step('element_is_not_visible')
    def element_is_not_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    @allure.step('element_is_clickable')
    def element_is_clickable(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    @allure.step('go_to_element')
    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('maximize_window')
    def maximize_window(self):
        self.driver.maximize_window()

    @allure.step('maximize_window')
    def full_screen_window(self):
        self.driver.fullscreen_window()

    @allure.step('window_scroll_-100')
    def window_scroll__100(self):
        self.driver.execute_script("window.scrollBy(0, -100);")

    @allure.step('window_scroll_100')
    def window_scroll_100(self):
        self.driver.execute_script("window.scrollBy(0, 100);")

    @allure.step('action_double_click')
    def action_double_click(self, element):
        action = ActionChains(self.driver)
        action.double_click(element)
        action.perform()

    @allure.step('action_right_click')
    def action_right_click(self, element):
        action = ActionChains(self.driver)
        action.context_click(element)
        action.perform()

    @allure.step('action_drag_and_drop_by_offset')
    def action_drag_and_drop_by_offset(self, element, x_coords, y_coords):
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(element, x_coords, y_coords)
        action.perform()

    @allure.step('action_drag_and_drop_to_element')
    def action_drag_and_drop_to_element(self, what, where):
        action = ActionChains(self.driver)
        action.drag_and_drop(what, where)
        action.perform()

    @allure.step('action_move_to_element')
    def action_move_to_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()

    @allure.step('element_is_not_present')
    def element_is_not_present(self, locator, timeout=4):
        try:
            wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))
        except TimeoutException:
            return True
        return False
