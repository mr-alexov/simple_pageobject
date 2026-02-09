import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from helpers import attach


@pytest.fixture
def browser():
    """Fixture for remote browser connection to Selenoid"""
    options = Options()
    options.add_argument("--start-maximized")
    
    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    # Если запускать локально
    # driver = webdriver.Chrome()
    
    yield driver

    attach.add_html(browser)
    attach.add_logs(browser)
    attach.add_screenshot(browser)

    driver.quit()
