import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class DemoMultipleWindows:
    def multiple_windows(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        parent_handle = self.driver.current_window_handle
        print(parent_handle)
        self.driver.find_element(By.XPATH, "//a[text()='OrangeHRM, Inc']").click()
        all_handles = self.driver.window_handles
        print(all_handles)
        for handle in all_handles:
            if handle != parent_handle:
                self.driver.switch_to.window(handle)
        self.driver.find_element(By.XPATH, "(//button[text()='Contact Sales'])[2]").click()
        time.sleep(2)
        self.driver.switch_to.window(parent_handle)
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        time.sleep(2)
        self.driver.quit()


demo = DemoMultipleWindows()
demo.multiple_windows()
