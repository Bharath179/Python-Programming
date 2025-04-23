import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Grouping tests with classes

"""class TestLogin():
    @pytest.fixture(scope="function")
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        yield self.driver
        time.sleep(2)
        self.driver.quit()

    def test_login(self,setup):
        self.driver=setup
        self.driver.find_element(By.NAME,"username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
        if self.driver.title=="OrangeHRM":
            print("Test is Passed")
        else:
            print("Test is failed")

    def test_invalidlogin(self,setup):
        self.driver=setup
        self.driver.find_element(By.NAME,"username").send_keys("Adminsd")
        self.driver.find_element(By.NAME, "password").send_keys("admin1234")
        self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
        # Wait for the error message to appear
        error_message = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[text()='Invalid credentials']"))
        )
        # Assert that the error message is displayed
        assert "Invalid credentials" in error_message.text"""

#Grouping tests with markers

@pytest.fixture(scope="function")
def setup():
    driver=webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    time.sleep(2)
    driver.quit()

@pytest.mark.smoke
def test_login(setup):
    driver=setup
    driver.find_element(By.NAME,"username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.XPATH,"//button[@type='submit']").click()
    if driver.title=="OrangeHRM":
        print("Test is Passed")
    else:
        print("Test is failed")

@pytest.mark.regression
def test_invalidlogin(setup):
    driver=setup
    driver.find_element(By.NAME,"username").send_keys("Adminsd")
    driver.find_element(By.NAME, "password").send_keys("admin1234")
    driver.find_element(By.XPATH,"//button[@type='submit']").click()
    # Wait for the error message to appear
    error_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[text()='Invalid credentials']"))
    )
    # Assert that the error message is displayed
    assert "Invalid credentials" in error_message.text

