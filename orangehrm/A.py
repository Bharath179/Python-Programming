from selenium.webdriver.common.by import By
from orangehrm import XLUtils
from selenium import webdriver

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

file="C:\\Users\\Lenovo\\Desktop\\data1.xlsx"
rows=XLUtils.getRowCount(file,"Sheet1")

for r in range(2,rows+1):
 username=XLUtils.readData(file,"Sheet1",r,1)
 password=XLUtils.readData(file,"Sheet1",r,2)

driver.find_element(By.ID,"user-name").send_keys(username)
driver.find_element(By.ID,"password").send_keys(password)
driver.find_element(By.ID,"login-button").click()
