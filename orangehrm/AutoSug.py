import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://seleniumpractise.blogspot.com/2016/08/how-to-handle-autocomplete-feature-in.html")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.ID,"tags").send_keys("S")
total_sugg=driver.find_elements(By.XPATH,"//li[@class='ui-menu-item']//div")
print("Total no of suggestions are:",len(total_sugg))
for ele in total_sugg:
    print(ele.text)
    if ele.text=="Selenium":
        print("Record found...")
        time.sleep(2)
        ele.click()
        break
    driver.close()



