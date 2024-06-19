import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()

allLinks=driver.find_element(By.TAG_NAME,'a')

count=0
for link in allLinks:
    url=link.get_attribute('href')
    try:
        res=requests.head(url)
    except:
        None

        if res.status_code>=400:
            print(url, "broken links")
            count+=1
        else:
            print(url, "Valid links")