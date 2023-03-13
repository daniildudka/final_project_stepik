from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pytest


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: ru, eng, etc...")
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")  # получаем параметр командной строки browser_name
    browser = None
    if browser_name == "chrome":
        print("\nstart Сhrome browser for test..")
        user_language = request.config.getoption("language")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
        # browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart Firefox browser for test..")
        user_language = request.config.getoption("language")
        options = Optionsf()
        options.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(options=options)
        # browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
