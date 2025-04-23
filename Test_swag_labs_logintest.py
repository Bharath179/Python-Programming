from selenium import webdriver
import unittest
import HtmlTestRunner
from selenium.webdriver.common.by import By

url = "https://www.saucedemo.com/v1/index.html"


class SwagLabsTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    def test_homepage_title(self):
        self.driver.get(url)
        self.assertEqual("Swag Labs", self.driver.title, "webpage title is not matching")

    def test_login(self):
        self.driver.get(url)
        self.driver.find_element(By.NAME, "user-name").send_keys("standard_user")
        self.driver.find_element(By.NAME, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        self.assertEqual("Swag Labs", self.driver.title, "webpage title is not matching")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Tested completed...")


if __name__ == '__main__':
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(output='reports')
    )
