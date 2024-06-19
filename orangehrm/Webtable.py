import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@name='password']").send_keys("admin123")
time.sleep(2)
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//a[@class='oxd-main-menu-item']//span[text()='Admin']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//nav[@aria-label='Topbar Menu']//span[text()='User Management ']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//ul[@class='oxd-dropdown-menu']//a[text()='Users']").click()
time.sleep(2)
rows=len(driver.find_elements(By.XPATH,"//div[@class='orangehrm-container']"))
print("Number of rows in a table:",rows)
