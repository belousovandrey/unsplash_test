from selenium.webdriver.common.by import By


class MainPageLocators:
    REGIONS_BUTTON = (By.CSS_SELECTOR, '[class="MuiBackdrop-root geo-tooltip__backdrop MuiBackdrop-invisible"]')
    COOKIE_BUTTON = (By.CSS_SELECTOR, '[class="MuiButtonBase-root MuiIconButton-root icon-button__root icon-button__root_size_default cookies-notification__button"]')
    # login_form
    MAIN_LOGIN_BUTTON = (By.CSS_SELECTOR, '[class="MuiButtonBase-root MuiButton-root MuiButton-outlined customer-header-login__button-initial"]')
    LOGIN = (By.CSS_SELECTOR, '[class="MuiInputBase-input MuiInput-input text-field__input"]')
    PASSWORD = (By.CSS_SELECTOR, '[class="MuiInputBase-input MuiInput-input text-field__input password-input__input MuiInputBase-inputAdornedEnd"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[class="MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-containedSecondary"]')
    LOGIN_ERROR = (By.CSS_SELECTOR, '[class="MuiFormHelperText-root Mui-error MuiFormHelperText-filled"]')
