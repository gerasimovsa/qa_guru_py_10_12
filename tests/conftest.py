import pytest
import allure
from selene import browser


@pytest.fixture(scope="function", autouse=True)
def setup_browser():
    with allure.step("Settings base url"):
        browser.config.base_url = "https://demoqa.com"
    with allure.step("Selecting Firefox for browser"):
        browser.config.driver_name = "firefox"
    with allure.step("Setting up timeout for browser"):
        browser.config.timeout = 6.0
    with allure.step("Setting up browser window size"):
        browser.config.window_width = 1920
        browser.config.window_height = 1200
    yield
    browser.quit()

