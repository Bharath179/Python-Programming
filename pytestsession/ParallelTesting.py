import pytest
from selenium import webdriver
import time


# Test case to open Google on Chrome
@pytest.mark.parametrize('browser', ['firefox', 'chrome'])
def test_google(browser):
    global driver
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()

    driver.get("https://www.google.com")
    assert "Google" in driver.title
    time.sleep(2)
    driver.quit()
