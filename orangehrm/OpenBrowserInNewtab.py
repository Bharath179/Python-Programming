import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.implicitly_wait(10)

#driver.get("https://demo.nopcommerce.com/")
#driver.maximize_window()
#reglink=Keys.CONTROL+Keys.RETURN
#driver.find_element(By.LINK_TEXT,"Register").send_keys(reglink)

#New-Tab -Selenium
driver.get("https://demo.nopcommerce.com/")
driver.switch_to.new_window('window')
driver.get("https://www.orangehrm.com/")
