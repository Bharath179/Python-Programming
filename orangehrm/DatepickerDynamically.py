import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
time.sleep(2)
driver.find_element(By.ID,"dob").click()
month=Select(driver.find_element(By.XPATH,"//select[@data-handler='selectMonth']"))
time.sleep(2)
month.select_by_visible_text("Apr")

year=Select(driver.find_element(By.XPATH,"//select[@data-handler='selectYear']"))
time.sleep(2)
year.select_by_visible_text("1997")

alldates=driver.find_elements(By.XPATH,"//*[@id='ui-datepicker-div']/table/tbody/tr/td/a")

for date in alldates:
    if date.text=="08":
        date.click()
        break