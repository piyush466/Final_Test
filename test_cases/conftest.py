import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options

from pages.base_file import Base
from pages.login_page import Login


def pytest_addoption(parser):
    parser.addoption("--browser", action='store', default='chrome')

@pytest.fixture
def setup(request):
    browser = request.config.getoption('--browser')
    option = Options()
    option.add_argument("--incognito")
    option.add_argument("--headless")
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        option = Options()
        option.add_argument("--headless")
        driver = webdriver.Firefox()
    elif browser == "safari":
        driver = webdriver.Safari()
    else:
        driver = webdriver.Chrome()

    driver.get("https://practicetestautomation.com/practice-test-login/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.login = Login(driver)
    request.cls.base = Base(driver)
    yield driver
    driver.quit()