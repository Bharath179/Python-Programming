from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.filemail.com/share/upload-file")
driver.maximize_window()

driver.find_element(By.XPATH,"//label[@id='addBtn']").click()

