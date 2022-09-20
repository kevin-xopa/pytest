from pytest import fixture

# import os
# from selenium import webdriver

# @fixture(scope='session')
# def chrome_browser():
#     chromedriver = "./driver/chromedriver"
#     os.environ["webdriver.chrome.driver"] = chromedriver
#     driver = webdriver.Chrome(chromedriver)
#     # return driver
#     yield driver

#     print('I am tearing down the browser...')

def pytest_addoption(parser):
    parser.addoption(
        '--env',
        action="store",
        help="Environment to run the tests against"
    )

@fixture(scope='session')
def env(request):
    return request.config.getoption('--env')