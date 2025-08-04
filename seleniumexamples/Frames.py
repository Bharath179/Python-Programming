import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class DemoFrames:
    def handle_frames(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.hyrtutorials.com/p/frames-practice.html")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH, "//iframe[@id='frm1']"))
        time.sleep(2)
        dropdown = Select(self.driver.find_element(By.XPATH, "//select[@id='course']"))
        time.sleep(2)
        dropdown.select_by_visible_text("Python")
        time.sleep(2)
        self.driver.switch_to.default_content()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@id='name']").send_keys("Admin")
        time.sleep(2)
        self.driver.quit()


demo = DemoFrames()
demo.handle_frames()
