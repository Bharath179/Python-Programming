from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(2)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
userTextfield=driver.find_element(By.XPATH,"//input[@name='username']")
userTextfield.send_keys("Admin")
driver.find_element(By.XPATH,"//input[@type='password']").send_keys("admin123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
driver.close()
driver.quit()
