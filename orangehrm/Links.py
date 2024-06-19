from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.nopcommerce.com/")
driver.implicitly_wait(10)
links=driver.find_elements(By.TAG_NAME,"a")
print("Number of links present is:",len(links))
for link in links:
    print(link.text)
