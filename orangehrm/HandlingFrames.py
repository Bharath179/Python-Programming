import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.implicitly_wait(5)
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()
driver.find_element(By.XPATH,"//a[text()='Iframe with in an Iframe']").click()
outerframe=driver.find_element(By.XPATH,"//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(outerframe)

innerframe=driver.find_element(By.XPATH,"//div[@class='iframe-container']//iframe")
driver.switch_to.frame(innerframe)
time.sleep(2)
driver.find_element(By.XPATH,"//input[@type='text']").send_keys("Welcome")