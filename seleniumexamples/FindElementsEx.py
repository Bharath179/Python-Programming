import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.yathra.com/")
driver.maximize_window()
driver.implicitly_wait(10)
lista=driver.find_elements(By.TAG_NAME,"a")
time.sleep(2)
print(len(lista))
for elements in lista:
    print(elements.text)
driver.quit()

