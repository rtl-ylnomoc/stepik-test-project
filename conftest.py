import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',  # cross-browser implementation
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: ru, en or etc")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption('browser_name')
    language = request.config.getoption('language')
    if browser_name == 'chrome':
        opt = Options()
        opt.add_experimental_option('prefs', {'intl.accept_languages': language})
        print("\nstart browser for test..")
        with webdriver.Chrome(options=opt) as browser:
            yield browser
            print('\nquit browser..')
    elif browser_name == 'firefox':
        profile = webdriver.FirefoxProfile()
        profile.set_preference('intl.accept_languages', language)
        print("\nstart browser for test..")
        with webdriver.Firefox(firefox_profile=profile) as browser:
            yield browser
            print('\nquit browser..')
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
