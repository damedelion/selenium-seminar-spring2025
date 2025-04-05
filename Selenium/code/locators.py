from selenium.webdriver.common.by import By

class BasePageLocators:
    AUTH_HEADER_BUTTON = (By.CLASS_NAME, 'gtm-auth-header-btn')
    SIGNUP_MODAL_LINK = (By.CLASS_NAME, 'gtm-signup-modal-link')
    EMAIL_INPUT = (By.NAME, 'email')
    PASSWORD_INPUT = (By.NAME, 'password')
    LOGIN_BUTTON = (By.CLASS_NAME, 'gtm-login-btn')


class MainPageLocators(BasePageLocators):
    PEOPLE_LINK = (By.XPATH, "//a[@href='/people/']")
    INPUT_TEXT = (By.CLASS_NAME, "input-text")
    INPUT_SUBMIT = (By.CLASS_NAME, "input-submit")
    REALNAME = (By.CLASS_NAME, "realname")
    SCHEDULE_LINK = (By.XPATH, "//a[@href='/schedule/']")
    LESSON_BY_NAME = lambda lesson_name: (By.XPATH, f"//a[contains(text(), '{lesson_name}')]")

