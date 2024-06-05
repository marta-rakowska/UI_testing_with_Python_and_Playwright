import time

import pytest
from playwright.sync_api import Page
from pages.search import SearchPage
from pages.main import MainPage

@pytest.fixture(scope='function')
def main_page(page):
    return MainPage(page)

@pytest.fixture(scope='function')
def search_page(page):
    return SearchPage(page)

@pytest.fixture(scope='function')
def page(page: Page):
    page.goto('https://automationexercise.com/')
    yield page

@pytest.fixture(scope='session', autouse=True)
def measure_time():
    start_time = time.time()
    yield
    end_time = time.time()
    print(end_time - start_time)

