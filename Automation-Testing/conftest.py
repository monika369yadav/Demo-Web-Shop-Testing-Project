"""
conftest.py — pytest automatically finds this file and shares fixtures
across all test files. The 'driver' fixture opens a browser before each
test and closes it after, so every test starts fresh.
"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    chrome_driver = webdriver.Chrome(service=service)
    chrome_driver.maximize_window()

    yield chrome_driver  # test runs here

    chrome_driver.quit()  # runs after the test finishes, pass or fail
