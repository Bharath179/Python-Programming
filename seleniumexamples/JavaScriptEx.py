import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class DemoOpenBrowser():
    def open_browser(self):
        self.driver = webdriver.Chrome()
        #self.driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        self.driver.execute_script("window.open('https://secure.yatra.com/social/common/yatra/signin.htm','_self')")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,1000)")
        time.sleep(5)
        self.driver.execute_script("window.scrollTo(0, 0)")
        continuebtn = self.driver.find_element(By.XPATH, "//button[text()='Continue']")
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();",continuebtn)
        time.sleep(2)
demo=DemoOpenBrowser()
demo.open_browser()