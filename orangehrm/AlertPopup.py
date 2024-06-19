import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

driver.find_element(By.XPATH,"//button[text()='Click for JS Confirm']").click()
time.sleep(2)

alertwindow=driver.switch_to.alert
print(alertwindow.text)
#alertwindow.send_keys("welcome")
alertwindow.accept()