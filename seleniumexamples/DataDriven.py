import XLUtility

import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class DemoAExcel:
    def data_driven(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        path = "C:\\Users\\Lenovo\\Desktop\\datadriven.xlsx"
        rows = XLUtility.getRowCount(path, "Sheet3")
        for r in range(2, rows + 1):
            username = XLUtility.readData(path, 'Sheet3', r, 1)
            password = XLUtility.readData(path, 'Sheet3', r, 2)
            self.driver.find_element(By.NAME, "username").send_keys(username)
            self.driver.find_element(By.NAME, "password").send_keys(password)
            self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

            if self.driver.title == "OrangeHRM":
                print("Test is Passed")
                XLUtility.writeData(path, 'Sheet3', r, 3, 'pass')
            else:
                print("Test is Failed")
                XLUtility.writeData(path, 'Sheet3', r, 3, 'fail')
            self.driver.find_element(By.XPATH, "//span[@class='oxd-userdropdown-tab']").click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//a[text()='Logout']").click()
            time.sleep(2)


demo = DemoAExcel()
demo.data_driven()
