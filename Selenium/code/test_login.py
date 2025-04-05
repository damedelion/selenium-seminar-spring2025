import pytest
from _pytest.fixtures import FixtureRequest
import locators
from selenium.webdriver.common.by import By
from ui.pages.base_page import BasePage


class BaseCase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.login_page = LoginPage(driver)
        self.main_page = MainPage(driver)
        if self.authorize:
            print('Do something for login')


@pytest.fixture(scope='session')
def credentials():
    return {
        "email": "some_email@example.com",
        "password": "some_password"
    }


@pytest.fixture(scope='session')
def cookies(credentials, config):
        pass


class LoginPage(BasePage):
    url = 'https://education.vk.company/'
    locators = locators.BasePageLocators

    def login(self, user, password):
        self.click(self.locators.AUTH_HEADER_BUTTON)
        self.click(self.locators.SIGNUP_MODAL_LINK)
        self.find(self.locators.EMAIL_INPUT).send_keys(user)
        self.find(self.locators.PASSWORD_INPUT).send_keys(password)
        self.click(self.locators.LOGIN_BUTTON)
        self.wait(5)
        return MainPage(self.driver)


class MainPage(BasePage):
    authorize = True
    url = 'https://education.vk.company/feed/'
    locators = locators.MainPageLocators

    def search_student(self, name):
        self.click(self.locators.PEOPLE_LINK)
        self.find(self.locators.INPUT_TEXT).send_keys(name)
        return MainPage(self.driver)
    
    def search_lesson(self, name):
        self.click(self.locators.SCHEDULE_LINK)
        self.click(self.locators.LESSON_BY_NAME(name))
        return MainPage(self.driver)



class TestLogin(BaseCase):
    authorize = True

    def test_login(self, credentials):
        self.login_page.login(credentials['email'], credentials['password'])
        self.wait(5)
        assert self.driver.current_url == "https://education.vk.company/feed/"


class TestStudentSearch(BaseCase):
    url = 'https://education.vk.company/feed/'

    def test_search_student(self, credentials):
        self.login_page.login(credentials['email'], credentials['password'])

        name = "Денисенко"
        self.main_page.search_student(name)
        realname = self.driver.find_element(By.CLASS_NAME, locators.StudentSearchPageLocators.REALNAME)
        assert name in realname.text


class TestLessonSearch(BaseCase):
    url = 'https://education.vk.company/feed/'

    def test_lesson_student(self, credentials):
        self.login_page.login(credentials['email'], credentials['password'])

        name = "End-to-End тесты на Python"
        self.main_page.search_lesson(name)
        assert "3 апр, 18:00" in self.main_page.page_source
        assert "Рассмотрим современные инструменты для тестирования веб-приложений." in self.main_page.page_source
        assert "Как прошло занятие?" in self.main_page.page_source
