import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class DemoScreenShot:
    def screen_shot(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        continuebtn = self.driver.find_element(By.XPATH, "//button[text()='Continue']")
        continuebtn.screenshot(".\\test.png")
        continuebtn.click()
        time.sleep(2)
        self.driver.get_screenshot_as_file("C:\\Users\\Lenovo\\Pictures\\error.png")
        time.sleep(2)
        self.driver.save_screenshot(".\\test1.png")
        time.sleep(2)
        self.driver.quit()


demo = DemoScreenShot()
demo.screen_shot()
