import json
from pytest import fixture
from config import Config
import os
from selenium import webdriver


chromedriver = "../driver/chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver

data_path = 'C:/Users/kevin/Documents/udemy/pytest/test/test_data.json'

def load_test_data(path):
    with open(path) as f:
        data = json.load(f)
        return data


# @fixture(params=[
#     webdriver.Chrome(chromedriver),
#     webdriver.Firefox(chromedriver),
#     webdriver.Edge(chromedriver)
# ])
# def chrome_browser(request):
#     # driver = webdriver.Chrome(chromedriver)
#     driver = request.param
#     drvr = driver()
#     yield drvr
#     drvr.quit()

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

@fixture(scope='session')
def app_config(env):
    cfg = Config(env)
    return cfg


@fixture(params=[load_test_data(data_path)])
def tv_brand(request):
    data = request.param
    return data