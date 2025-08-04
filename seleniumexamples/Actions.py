import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

#MouseHover
"""class DemoActions():
    def handle_actions(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.myntra.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        menBtn=self.driver.find_element(By.XPATH,"(//a[text()='Men'])[1]")
        action=ActionChains(self.driver)
        action.move_to_element(menBtn).perform()
        time.sleep(2)
        self.driver.quit()
demo=DemoActions()
demo.handle_actions()"""

#CotextClick
"""class DemoActions():
    def handle_actions(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        menBtn=self.driver.find_element(By.XPATH,"//a[text()='OrangeHRM, Inc']")
        action=ActionChains(self.driver)
        action.context_click(menBtn).perform()
        time.sleep(2)
        self.driver.quit()
demo=DemoActions()
demo.handle_actions()"""


# Drag and Drop
class DemoActions:
    def handle_actions(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.myntra.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        drag = self.driver.find_element(By.XPATH, "//a[text()='Studio']")
        drop = self.driver.find_element(By.XPATH, "//input[@placeholder='Search for products, brands and more']")
        action = ActionChains(self.driver)
        action.drag_and_drop(drag, drop).perform()
        time.sleep(2)
        self.driver.quit()


demo = DemoActions()
demo.handle_actions()
