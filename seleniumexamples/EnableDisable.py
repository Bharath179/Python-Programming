from selenium import webdriver
from selenium.webdriver.common.by import By


class DemoEnableDisable:
    def check_enable_disable_button(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://training.openspan.com/login")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        state = self.driver.find_element(By.ID, "login_button").is_enabled()
        print(state)
        self.driver.find_element(By.ID, "user_name").send_keys("python")
        self.driver.find_element(By.ID, "user_pass").send_keys("python@123")
        state1 = self.driver.find_element(By.ID, "login_button").is_enabled()
        print(state1)
        self.driver.quit()


demo = DemoEnableDisable()
demo.check_enable_disable_button()
