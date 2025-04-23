
from selenium import webdriver
from selenium.webdriver.common.by import By

class DemoCheckBox():
    def check_checkbox_selected_or_not(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://demo.nopcommerce.com/login?returnurl=%2F")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
        state=self.driver.find_element(By.XPATH,"//input[@type='checkbox']").is_selected()
        print(state)
        self.driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
        state1 = self.driver.find_element(By.XPATH, "//input[@type='checkbox']").is_selected()
        print(state1)
        self.driver.quit()
demo = DemoCheckBox()
demo.check_checkbox_selected_or_not()
