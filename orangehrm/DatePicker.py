import time

from selenium import  webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

driver.switch_to.frame(0)
time.sleep(2)
driver.find_element(By.ID,"datepicker").send_keys("04/08/1997")
