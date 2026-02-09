import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def browser():
    """Fixture for remote browser connection to Selenoid"""
    options = Options()
    options.add_argument("--start-maximized")
    
    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    # driver = webdriver.Chrome()
    
    yield driver
    
    driver.quit()
