import time
import unittest
import HtmlTestRunner
from selenium import webdriver
import sys
sys.path.append("C:\\Users\\Lenovo\\PycharmProjects\\pythonProject")
from page_objects.Login_page import LoginPage

class LoginTest(unittest.TestCase):
    baseURL="https://www.saucedemo.com/v1/index.html"
    username="standard_user"
    password="secret_sauce"

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    def test_login(self):
        lp=LoginPage(self.driver)
        lp.set_username(self.username)
        lp.set_password(self.password)
        lp.click_login()
        time.sleep(2)
        self.assertEqual("Swag Labs","webpage of title is verified and it is correct")
        lp.click_menu()
        time.sleep(2)
        lp.click_logout()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test Completed...")

if __name__=="__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='.\\reports'))





