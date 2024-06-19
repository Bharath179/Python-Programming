import time

from selenium import  webdriver
from selenium.webdriver.common.by import By
import os
os.getcwd()

def chrome_setUp():
    driver=webdriver.Chrome()
    driver.implicitly_wait(5)

    return driver

driver=chrome_setUp()
driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.XPATH,"//*[@id='table-files']/tbody/tr[1]/td[5]/a").click()
time.sleep(5)
driver.quit()