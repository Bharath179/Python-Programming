import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.nopcommerce.com/")
time.sleep(5)
driver.find_element(By.XPATH,"//a[text()='Register']").click()
act_title=driver.title
exp_title="nopCommerce demo store. Register"
if act_title==exp_title:
    print("Passed")
else:
    print("Failed")
