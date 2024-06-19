import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.bbc.com")
driver.maximize_window()

#scroll down page by pixel
time.sleep(3)
driver.execute_script("window.scrollBy(0,3000)","")
#value=driver.execute_script("return window.pageYOffset;")
#print("Number of pixels moved:",value)

#scroll down page till the element is visible
element=driver.find_element(By.XPATH,"//h2[text()='Innovation']")
time.sleep(5)
driver.execute_script("arguments[0].scrollIntoView();",element)
time.sleep(4)
value=driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved:",value)

