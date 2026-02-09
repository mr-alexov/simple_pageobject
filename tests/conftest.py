import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from helpers import attach


@pytest.fixture
def browser():
    """Fixture for remote browser connection to Selenoid"""
    options = Options()
    options.add_argument("--start-maximized")

    remote = True  # Устанавливаем флаг для выбора между удаленным и локальным запуском

    if remote:
        driver = webdriver.Remote(
            command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
            options=options
        )
    else:
        # Если запускать локально
        driver = webdriver.Chrome()
    
    yield driver


    attach.add_logs(driver)
    attach.add_screenshot(driver)
    attach.add_html(driver)

    driver.quit()
