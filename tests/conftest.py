import pytest
import allure
from selene import browser
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from utils import attach


@pytest.fixture(scope="function", autouse=True)
def setup_browser():
    with allure.step("Settings base url"):
        browser.config.base_url = "https://demoqa.com"
    with allure.step("Setting up timeout for browser"):
        browser.config.timeout = 10.0
    with allure.step("Setting up browser window size"):
        browser.config.window_width = 1920
        browser.config.window_height = 1200
    with allure.step("Setting up Selenoid remote executor"):
        options = Options()
        selenoid_capabilities = {
            "browserName": "firefox",
            "browserVersion": "123.0",
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": True
            }
        }
        options.capabilities.update(selenoid_capabilities)
        driver = webdriver.Remote(
            command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
            options=options)
        browser.config.driver = driver

    yield

    attach.add_html(browser)
    attach.add_logs(browser)
    attach.add_screenshot(browser)
    attach.add_video(browser)

    browser.quit()
