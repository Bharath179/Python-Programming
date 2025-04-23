import time

from selenium import webdriver
from selenium.webdriver.common.by import By

#Alert Popup

"""class DemoPopups():
    def handle_popups(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://practice-automation.com/popups/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH,"//b[text()='Alert Popup']").click()
        alertpop=self.driver.switch_to.alert
        time.sleep(2)
        text=alertpop.text
        print(text)
        alertpop.accept()
        time.sleep(2)
        self.driver.quit()
demo=DemoPopups()
demo.handle_popups()"""

#Conformation PopUp

"""class DemoPopups():
    def handle_popups(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://practice-automation.com/popups/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH,"//button[@id='prompt']").click()
        alertpop=self.driver.switch_to.alert
        time.sleep(2)
        alertpop.send_keys("Admin")
        time.sleep(2)
        alertpop.accept()
        time.sleep(2)
        self.driver.quit()
demo=DemoPopups()
demo.handle_popups()"""

#Notification PopUp

"""class DemoPopups():
    def handle_popups(self):
        notification = webdriver.ChromeOptions()
        notification.add_argument("--disable-notifications")
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.homedepot.com/")
        time.sleep(2)
        self.driver.quit()
demo=DemoPopups()
demo.handle_popups()"""

#Authentation Popup
class DemoPopups():
    def handle_popups(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.quit()
demo=DemoPopups()
demo.handle_popups()