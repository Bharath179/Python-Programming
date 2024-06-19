import time

from selenium import webdriver

ops=webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")
driver=webdriver.Chrome()
time.sleep(4)
driver.get("https://whatmylocation.com/")
time.sleep(4)
driver.maximize_window()
time.sleep(2)