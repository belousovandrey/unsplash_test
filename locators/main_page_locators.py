from selenium.webdriver.common.by import By


class MainPageLocators:
    # login_form
    LOG_IN_BUTTON = (By.CSS_SELECTOR, '[class="cLLOA p1cWU jpBZ0 EzsBC KHq0c XHI2L"]')
    EMAIL = (By.CSS_SELECTOR, '#user_email')
    PASSWORD = (By.CSS_SELECTOR, '#user_password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[class="btn btn-default btn-block-level"]')
    LOGIN_ERROR = (By.CSS_SELECTOR, '[class="col-xs-10 col-sm-6 center-block flash__message"]')
    # reg_form
    REG_BUTTON = (By.XPATH, '/html/body/div[2]/div/div/div/div/div[4]/a')
    FIRST_NAME = (By.CSS_SELECTOR, '#user_first_name')
    LAST_NAME = (By.CSS_SELECTOR, '#user_last_name')
    USER_NAME = (By.CSS_SELECTOR, '#user_username')
    REG_PASSWORD = (By.CSS_SELECTOR, '#user_password')
    REG_FIN_BUTTON = (By.CSS_SELECTOR, '[class="btn btn-default btn-block-level"]')
    GOOD_REG = (By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/text()[2]')
    # Menu
    MENU_RIGHT = (By.CSS_SELECTOR, '[class="YbtJk jpBZ0 LCoFy cC9j1"]')
    MENU_ITEM = (By.XPATH, '#app > div > div.b4j4s > div > div > div.BK8tG > div > div.pRk2s > div.VCR4P > ul > li:nth-child(2) > a')
    MENU_ITEM = (By.XPATH, '//*[@id="app"]/div/div[2]/div/div/div[3]/div/div[2]/div[2]/ul/li[3]/a')
