from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"//a[text()='Create new account']").click()
dropdown=driver.find_element(By.NAME,"birthday_month").click()
select=Select
select.select_by_index(4)

alloptions=select.options
print(len(alloptions))

for opt in alloptions:
    print(opt.text)

    #select option from dropdown without using built-in methods
    for opt in alloptions:
        if opt.text=="Apr":
            opt.click()