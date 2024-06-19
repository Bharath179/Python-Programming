import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Edge()
driver.get("https://www.facebook.com/")
#driver.maximize_window()
driver.fullscreen_window()
driver.implicitly_wait(5)
time.sleep(5)
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(5)
driver.close()